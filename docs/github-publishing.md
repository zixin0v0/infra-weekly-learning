# GitHub 发布说明

现有远程仓库为 [zixin0v0/infra-weekly-learning](https://github.com/zixin0v0/infra-weekly-learning)，public，默认分支 `main`；本地工作目录名为 `infra-learning`。本次核对日期：2026-10-01。沿用现有仓库与分支，无需重新初始化或创建远程。

## 哪些内容同步

学习指南应同步：自学规则、24 段学习指南、带日期的资料复核、来源版本、原创概念图与导航一起保存，才能追踪学习安排如何调整。实际动手后的代码、配置、小型真实原始数据和报告也应同步，学习状态依据真实验收。

范围与入口见 [前八个学习位置](first-eight-weeks.md)，职责与运行归档见 [文件管理](repository-layout.md)。

`.gitignore` 已排除本地环境、模型权重、checkpoint 和大型 profiler 文件。实验小型原始数据、绘图代码、图表和报告应纳入版本管理，便于复现。

完整第三方 PDF/源码下载留临时目录；环境凭据不提交。`.log` 默认忽略，需要追溯的小型可公开输出保存成明确的 txt/CSV 摘录，报告标注大型文件位置及生成命令。

## 提交与推送流程

先检查改动与当前分支，确认相对链接、阅读预算、来源记录与实际学习状态：

```shell
git status --short
git diff --check
git branch --show-current
git remote -v
```

只暂存本次任务文件。例如单份文档可以用 `git add -- docs/first-eight-weeks.md`；本次完整学习指南还包括各周、导航、模板与来源记录。暂存后用 `git diff --cached --stat` 和 `git diff --cached --check` 再核对，随后提交。

```shell
git commit -m "Prepare first eight learning units"
git fetch origin main
git merge-base --is-ancestor origin/main HEAD
```

最后一条退出码为 0 才表明远程 main 是当前提交的祖先；否则先比较并整合远程更新。不要使用 force 推送覆盖他人的提交。

本次 Codex worktree 处于 detached HEAD。提交后从当前 HEAD 普通快进推送，不切换另一工作目录正在使用的 main：

```shell
git push origin HEAD:main
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

对比后两条的 commit SHA 确认远程接收，再从 GitHub 的自学总入口打开周导航与新增文件。常规 main checkout 也可用 `git push origin main`。推送结果以命令和远程核验为准，文档准备完成不代表已经推送成功。

许可证尚未选择，仓库不预填授权声明。链接到外部课程或项目时保留原始来源；后续引入第三方代码时记录来源版本及其许可。

暂时采用纯 Markdown，在 GitHub 和本地编辑器直接阅读。等内容积累后，再根据需要引入文档站或自动化，不增加初期学习负担。
