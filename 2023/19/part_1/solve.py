from __future__ import annotations

import os
from dataclasses import dataclass


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

    def __call__(self, rating: dict) -> str:
        val = rating[self.cat]

        if (self.greater_than and val > self.number) or (
            not self.greater_than and val < self.number
        ):
            if self.out_t == "A" or self.out_t == "R":
                return self.out_t
            return self.out_t(rating)

        if self.out_f == "A" or self.out_f == "R":
            return self.out_f
        return self.out_f(rating)


def parse_rating(line):
    ratings = {}
    for r in line.strip()[1:-1].split(","):
        splitted_rating = r.split("=")
        ratings[splitted_rating[0]] = int(splitted_rating[1])

    return ratings


def solve(lines: str) -> None:
    parsing_workflows = True
    workflows = {}
    ratings = []

    for line in lines:
        if len(line.strip()) == 0:
            parsing_workflows = False
            continue

        if parsing_workflows:
            s = line.strip().split("{")
            name, rules = s[0], s[1][:-1]
            workflows[name] = rules

        else:
            ratings.append(parse_rating(line.strip()))

    tree = Node.from_workflows(workflows, "in")

    output = 0

    for rating in ratings:
        if tree(rating) == "A":
            output += sum(rating.values())

    print(output)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
