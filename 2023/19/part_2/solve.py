from __future__ import annotations

import os
from dataclasses import dataclass
from copy import deepcopy
import math

@dataclass
class Node:
    cat: str
    greater_than: bool
    number: int
    out_t: Node | str
    out_f: Node | str

    @staticmethod
    def from_workflows(workflows, name):
        rules = workflows[name]

        rule = rules.split(",")[0]
        remaining = rules.replace(rule, "")[1:]

        if rule == "A" or rule == "R":
            return rule

        if ":" in rule:
            decision, out = rule.split(":")

            if ">" in decision:
                cat, number = decision.split(">")
                number = int(number)
                greater_than = True

            if "<" in decision:
                cat, number = decision.split("<")
                number = int(number)
                greater_than = False

            if out == "A" or out == "R":
                next_node_t = out
            else:
                next_node_t = Node.from_workflows(workflows, out)

            workflows["node_f"] = remaining
            next_node_f = Node.from_workflows(workflows, "node_f")

            return Node(cat, greater_than, number, next_node_t, next_node_f)

        return Node.from_workflows(workflows, rule)

    def __call__(self, ratings: dict) -> int:
        ratings_t = deepcopy(ratings)
        ratings_f = deepcopy(ratings)

        if self.greater_than and self.number >= ratings[self.cat][0]:
            ratings_t[self.cat][0] = self.number + 1
            ratings_f[self.cat][1] = self.number

        if not self.greater_than and self.number <= ratings[self.cat][1]:
            ratings_t[self.cat][1] = self.number - 1
            ratings_f[self.cat][0] = self.number

        output = 0

        if self.out_t == "A":
            output += math.prod(r[1] - r[0] + 1 for r in ratings_t.values())
        elif self.out_t != "R":
            output += self.out_t(ratings_t)
        
        if self.out_f == "A":
            output += math.prod(r[1] - r[0] + 1 for r in ratings_f.values())
            print(ratings_t)
        elif self.out_f != "R":
            output += self.out_f(ratings_f)

        return output


def solve(lines: str) -> None:
    parsing_workflows = True
    workflows = {}

    for line in lines:
        if len(line.strip()) == 0:
            parsing_workflows = False
            continue

        if parsing_workflows:
            s = line.strip().split("{")
            name, rules = s[0], s[1][:-1]
            workflows[name] = rules

    ratings = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}

    tree = Node.from_workflows(workflows, "in")

    print(tree(ratings))


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
