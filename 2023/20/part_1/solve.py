from __future__ import annotations
import os
from dataclasses import dataclass, field


@dataclass
class FlipFlop:
    state: bool = field(init=False, default=False)

    def __call__(self, pulse: bool) -> bool | None:
        if not pulse:
            self.state = not self.state
            return self.state


@dataclass
class Conjunction:
    states: dict

    def __call__(self, inp: str, pulse: bool) -> bool:
        self.states[inp] = pulse

        if self._all_high:
            return False

        return True

    @property
    def _all_high(self) -> bool:
        return all(self.states.values())
    

def push_button(modules: dict):
    next = []
    pulses = 1

    for dest in modules["broadcaster"]:
        m = modules[dest]

        if isinstance(m["module"], FlipFlop):
            out = m["module"](False)
        else:
            out = m["module"](dest, False)

        if out is not None:
            pulses += 1
            next.append((m["dest"], out))

    while len(next) > 0:
        next_new = []
        for n in next:
            m = modules[n[0]]

            if isinstance(m["module"], FlipFlop):
                out = m["module"](n[1])
            else:
                out = m["module"](n[0], n[1])

            if out is not None:
                pulses += 1
                next_new.append((m["dest"], out))

        next = next_new

    return pulses


def solve(lines: str) -> None:
    modules = {}
    module_names = ["broadcaster"]

    for line in lines:
        src = line.split(" -> ")[0]

        if src != "broadcaster":
            module_names.append(src[1:])

    for line in lines:
        src, dests = line.strip().split(" -> ")

        if src.startswith("%"):
            modules[src[1:]] = {"module": FlipFlop(), "dest": dests}

        elif src.startswith("&"):
            modules[src[1:]] = {
                "module": Conjunction({name: False for name in module_names}),
                "dest": dests,
            }

        else:
            modules[src] = dests.split(", ")

    print(push_button(modules))


if __name__ == "__main__":
    input_file = "sample_input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
