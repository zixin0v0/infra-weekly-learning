"""串行故障模拟：效果已经发生，第一次确认丢失。deduplicated 模式需要补全。"""

import argparse
import json


class CounterService:
    def __init__(self):
        self.value = 0
        self.completed = {}

    def apply_naively(self, task_id, amount):
        if not isinstance(task_id, str) or not task_id:
            raise ValueError("task_id 必须为非空字符串")
        if type(amount) is not int or amount <= 0:
            raise ValueError("amount 必须为正整数")
        self.value += amount
        return self.value

    def apply_once(self, task_id, amount):
        raise NotImplementedError("同 task_id 和 amount 返回首次结果；相同 ID 不同 amount 拒绝；新任务才改变 value")


def replay(service, deduplicated=False):
    events = []
    apply = service.apply_once if deduplicated else service.apply_naively
    for attempt_id, confirmed in ((1, False), (2, True)):
        before = service.value
        result = apply("request-A", 2)
        events.append({"task_id": "request-A", "attempt_id": attempt_id,
                       "effect_delta": service.value - before, "result": result,
                       "client_event": "reply_received" if confirmed else "timeout_after_effect"})
    return {"simulation": True, "events": events, "counter": service.value}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("naive", "deduplicated"), default="naive")
    arguments = parser.parse_args()
    print(json.dumps(replay(CounterService(), arguments.mode == "deduplicated"),
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
