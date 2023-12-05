import os
from dataclasses import dataclass
from typing import List

@dataclass
class Map:
    dest_range_start: int
    source_range_start: int
    range_length: int

@dataclass
class Maps:
    seeds: List[int]
    seed_to_soil: Map
    soil_to_fertilizer: Map
    fertilizer_to_water: Map
    water_to_light: Map
    light_to_temp: Map
    temp_to_humidity: Map
    himidity_to_location: Map


def parse_maps(inp: str):
    inp = [i.strip() for i in inp]
    seeds = map(int, (inp[0].split(": ")[-1].strip().split(" ")))

    s_to_s_index = inp.index("seed-to-soil map:")


def solve(inp: str) -> None:
    parse_maps(inp)

if __name__ == "__main__":
    input_file = "sample_input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
