from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Map:
    dest_range_start: int
    source_range_start: int
    range_length: int

    def in_range(self, source_value) -> bool:
        return (
            source_value >= self.source_range_start
            and source_value < self.source_range_start + self.range_length
        )

    def __call__(self, source_value) -> int:
        return source_value - self.source_range_start + self.dest_range_start


@dataclass
class Maps:
    maps: List[Map]

    @staticmethod
    def from_lines(lines: List[str]) -> Maps:
        maps = [Map(*map(int, line.split(" "))) for line in lines]
        return Maps(maps)

    def __call__(self, source_value) -> int:
        dest_value = source_value

        for map in self.maps:
            if map.in_range(source_value):
                dest_value = map(source_value)
                break

        return dest_value


@dataclass
class Pipeline:
    seed_to_soil: Map
    soil_to_fertilizer: Map
    fertilizer_to_water: Map
    water_to_light: Map
    light_to_temp: Map
    temp_to_humidity: Map
    himidity_to_location: Map

    def __call__(self, seed) -> int:
        soil = self.seed_to_soil(seed)
        fertilizer = self.soil_to_fertilizer(soil)
        water = self.fertilizer_to_water(fertilizer)
        light = self.water_to_light(water)
        temp = self.light_to_temp(light)
        humidity = self.temp_to_humidity(temp)
        location = self.himidity_to_location(humidity)

        return location


def parse_maps(inp: str) -> Tuple[List[int], Pipeline]:
    inp = [i.strip() for i in inp]
    seeds = map(int, (inp[0].split(": ")[-1].strip().split(" ")))

    start_index = inp.index("seed-to-soil map:") + 1
    end_index = start_index + inp[start_index:].index("")

    seed_to_soil_maps = Maps.from_lines(inp[start_index:end_index])

    start_index = inp.index("soil-to-fertilizer map:") + 1
    end_index = start_index + inp[start_index:].index("")

    soil_to_fertilizer_maps = Maps.from_lines(inp[start_index:end_index])

    start_index = inp.index("fertilizer-to-water map:") + 1
    end_index = start_index + inp[start_index:].index("")

    fertilizer_to_water_maps = Maps.from_lines(inp[start_index:end_index])

    start_index = inp.index("water-to-light map:") + 1
    end_index = start_index + inp[start_index:].index("")

    water_to_light_maps = Maps.from_lines(inp[start_index:end_index])

    start_index = inp.index("light-to-temperature map:") + 1
    end_index = start_index + inp[start_index:].index("")

    light_to_temp_maps = Maps.from_lines(inp[start_index:end_index])

    start_index = inp.index("temperature-to-humidity map:") + 1
    end_index = start_index + inp[start_index:].index("")

    temp_to_humidity_maps = Maps.from_lines(inp[start_index:end_index])

    start_index = inp.index("humidity-to-location map:") + 1

    humidity_to_location_maps = Maps.from_lines(inp[start_index:])

    return seeds, Pipeline(
        seed_to_soil_maps,
        soil_to_fertilizer_maps,
        fertilizer_to_water_maps,
        water_to_light_maps,
        light_to_temp_maps,
        temp_to_humidity_maps,
        humidity_to_location_maps,
    )


def solve(inp: str) -> None:
    seeds, pipeline = parse_maps(inp)

    output = min(map(pipeline, seeds))
    print(output)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
