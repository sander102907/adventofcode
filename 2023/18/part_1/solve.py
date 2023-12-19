import os
from dataclasses import dataclass
from typing import List
from shapely import Point, Polygon

@dataclass
class Instruction:
    direction: str
    meters: int
    colour: str

    def __post_init__(self):
        self.meters = int(self.meters)

def dig(dig_plan: List[Instruction]):
    start = Point(0, 0)

    points = [start]
    m3 = 0

    for instruction in dig_plan:
        m3 += instruction.meters
        if instruction.direction == "U":
            new_point = Point(points[-1].x, points[-1].y - instruction.meters)
        if instruction.direction == "R":
            new_point = Point(points[-1].x + instruction.meters, points[-1].y)
        if instruction.direction == "L":
            new_point = Point(points[-1].x - instruction.meters, points[-1].y)
        if instruction.direction == "D":
            new_point = Point(points[-1].x, points[-1].y + instruction.meters)

        points.append(new_point)

    return Polygon(points), m3


def solve(lines: str) -> None:
    dig_plan = [Instruction(*line.strip().split(" ")) for line in lines]

    polygon, m3 = dig(dig_plan)

    print(m3 + polygon.area - m3 / 2 + 1)

if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
