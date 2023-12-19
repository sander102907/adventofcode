import os
from dataclasses import dataclass
from typing import List
from shapely import Point, Polygon

@dataclass
class Instruction:
    direction: int
    meters: int

    @staticmethod
    def from_string(line: str):
        instr = line.strip().split(" ")[-1]

        meters = int(instr[2:7], 16)
        direction = int(instr[7], 16)

        return Instruction(direction, meters)

    def __post_init__(self):
        self.meters = int(self.meters)

def dig(dig_plan: List[Instruction]):
    start = Point(0, 0)

    points = [start]
    m3 = 0

    for instruction in dig_plan:
        m3 += instruction.meters
        if instruction.direction == 3:
            new_point = Point(points[-1].x, points[-1].y - instruction.meters)
        if instruction.direction == 0:
            new_point = Point(points[-1].x + instruction.meters, points[-1].y)
        if instruction.direction == 2:
            new_point = Point(points[-1].x - instruction.meters, points[-1].y)
        if instruction.direction == 1:
            new_point = Point(points[-1].x, points[-1].y + instruction.meters)

        points.append(new_point)

    return Polygon(points), m3


def solve(lines: str) -> None:
    dig_plan = [Instruction.from_string(line) for line in lines]

    polygon, m3 = dig(dig_plan)

    print(m3 + polygon.area - m3 / 2 + 1)

if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
