from pathlib import Path
import re
import sys
import struct
import unicodedata
from urllib.parse import unquote
from xml.etree import ElementTree


def heading_slug(value):
    value = re.sub(r"<[^>]*>", "", value)
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = value.lower()
    return "".join(
        character
        for character in value
        if character in " -_" or unicodedata.category(character)[0] in "LN"
    ).replace(" ", "-")


def visible_markdown(content):
    output = []
    fence = None
    for line in content.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            output.append(line)
    return "\n".join(output), fence is None


def document_anchors(content):
    result = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"\s*></a>', content))
    counts = {}
    for match in re.finditer(r"^#{1,6}\s+(.+?)\s*#*\s*$", content, re.MULTILINE):
        base = heading_slug(match.group(1))
        count = counts.get(base, 0)
        counts[base] = count + 1
        result.add(base if count == 0 else f"{base}-{count}")
    return result


def check_repository(root):
    markdown_files = sorted(
        path for path in root.rglob("*.md")
        if not any(part in {".git", ".venv", "venv", "node_modules"} for part in path.relative_to(root).parts)
    )
    errors = []
    contents = {}
    anchors = {}
    link_count = 0
    image_count = 0
    referenced_figures = set()
    for path in markdown_files:
        content, closed = visible_markdown(path.read_text(encoding="utf-8-sig"))
        contents[path.resolve()] = content
        anchors[path.resolve()] = document_anchors(content)
        if not closed:
            errors.append(f"{path.relative_to(root)}: unclosed code fence")
        if len(re.findall(r"<details(?:\s[^>]*)?>", content)) != content.count("</details>"):
            errors.append(f"{path.relative_to(root)}: unbalanced details")
        if "@/" in content:
            errors.append(f"{path.relative_to(root)}: unresolved root marker")
        if re.search(r"教师|学生|授课|交作业|批改|教学管理", content):
            errors.append(f"{path.relative_to(root)}: non-personal wording")
    for path, content in contents.items():
        for label in re.findall(r"\[([^\]\n]+)\]\([^)\n]+\)", content):
            if re.search(r'</?a\b|\bid\s*=\s*["\']', label):
                errors.append(f"{path.relative_to(root)}: anchor markup used as visible link text")
        for match in re.finditer(r"!\[([^\]\n]*)\]\((<[^>]+>|[^)\n]+)\)", content):
            image_count += 1
            alternative, target = match.groups()
            if len(alternative.strip()) < 4:
                errors.append(f"{path.relative_to(root)}: image needs descriptive alternative text")
            target = target.split(' "')[0].strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                continue
            destination = (path.parent / unquote(target).partition("#")[0]).resolve()
            if destination.is_relative_to(root / "assets" / "figures"):
                referenced_figures.add(destination.stem)
                if destination.suffix != ".png":
                    errors.append(f"{path.relative_to(root)}: embed PNG and link SVG separately: {target}")
                if not destination.with_suffix(".svg").is_file():
                    errors.append(f"{path.relative_to(root)}: missing SVG export: {target}")
        for match in re.finditer(r"\]\((<[^>]+>|[^)\n]+)\)", content):
            target = match.group(1).split(' "')[0].strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                continue
            link_count += 1
            target_path, _, fragment = unquote(target).partition("#")
            destination = (path.parent / target_path).resolve() if target_path else path
            if not destination.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: link escapes repository: {target}")
            elif not destination.exists():
                errors.append(f"{path.relative_to(root)}: missing target: {target}")
            else:
                cursor = root
                for part in destination.relative_to(root).parts:
                    if part not in {entry.name for entry in cursor.iterdir()}:
                        errors.append(f"{path.relative_to(root)}: path case mismatch: {target}")
                        break
                    cursor = cursor / part
                if fragment and destination.suffix == ".md" and fragment not in anchors.get(destination, set()):
                    errors.append(f"{path.relative_to(root)}: missing anchor: {target}")
    figure_directory = root / "assets" / "figures"
    png_names = {path.stem for path in figure_directory.glob("*.png")}
    svg_names = {path.stem for path in figure_directory.glob("*.svg")}
    if png_names != svg_names:
        errors.append(f"unpaired PNG/SVG exports: {sorted(png_names ^ svg_names)}")
    for unused in sorted((png_names | svg_names) - referenced_figures):
        errors.append(f"figure has no Markdown image reference: {unused}")
    for figure_path in sorted(figure_directory.glob("*.png")):
        with figure_path.open("rb") as stream:
            header = stream.read(24)
        if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
            errors.append(f"invalid PNG export: {figure_path.name}")
        elif min(struct.unpack(">II", header[16:24])) < 600:
            errors.append(f"PNG export too small for reading: {figure_path.name}")
    for figure_path in sorted(figure_directory.glob("*.svg")):
        try:
            svg = ElementTree.parse(figure_path).getroot()
            if svg.tag != "{http://www.w3.org/2000/svg}svg" or "viewBox" not in svg.attrib:
                errors.append(f"invalid SVG root or missing viewBox: {figure_path.name}")
        except ElementTree.ParseError:
            errors.append(f"invalid SVG XML: {figure_path.name}")
    expected_docs = {"README.md", "design.md", "maintenance.md", "coverage.md"}
    actual_docs = {path.name for path in (root / "docs").glob("*.md")}
    if actual_docs != expected_docs:
        errors.append(f"docs root differs: {sorted(actual_docs)}")
    for prefix, count, directory in [("p", 8, "foundations"), ("s", 6, "bridges")]:
        for number in range(1, count + 1):
            path = root / "course" / directory / f"{prefix}{number:02}.md"
            if not path.is_file():
                errors.append(f"missing learning page: {path.relative_to(root)}")
    units = sorted((root / "weeks").glob("week-*"))
    if len(units) != 16:
        errors.append(f"expected 16 units, found {len(units)}")
    for unit in units:
        number = int(unit.name.split("-")[1])
        sessions = sorted(unit.glob("session-*.md"))
        if not sessions or not (unit / "assessment.md").is_file():
            errors.append(f"{unit.name}: missing sessions or assessment")
        if (unit / "study-guide.md").exists():
            errors.append(f"{unit.name}: obsolete duplicate study guide")
        for index, session in enumerate(sessions):
            content = contents[session.resolve()]
            if "[上一课]" not in content or "[下一课]" not in content:
                errors.append(f"{session.relative_to(root)}: missing lesson navigation")
            previous = sessions[index - 1].name if index else "README.md"
            following = sessions[index + 1].name if index + 1 < len(sessions) else "assessment.md"
            if f"[上一课]({previous})" not in content or f"[下一课]({following})" not in content:
                errors.append(f"{session.relative_to(root)}: lesson navigation skips a session")
        assessment = unit / "assessment.md"
        if assessment.exists() and f"w{number}" not in anchors[assessment.resolve()]:
            errors.append(f"{unit.name}: missing stable assessment anchor")
    print(f"Markdown: {len(markdown_files)}; local links: {link_count}; units: {len(units)}")
    print(f"Image references: {image_count}; PNG/SVG pairs: {len(png_names & svg_names)}")
    for error in errors:
        print(error)
    print(f"{'FAIL' if errors else 'PASS'}: {len(errors)} errors")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(check_repository(Path(__file__).resolve().parents[1]))
