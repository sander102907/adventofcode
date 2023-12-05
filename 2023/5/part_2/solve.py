from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class SeedRange:
    start: int
    range: int

    @property
    def end(self) -> int:
        return self.start + self.range


@dataclass
class Map:
    dest_start: int
    source_start: int
    range_length: int

    def in_range(self, source_value) -> bool:
        return (
            source_value >= self.source_start
            and source_value < self.source_start + self.range_length
        )

    @property
    def source_end(self) -> int:
        return self.source_start + self.range_length

    def overlap(self, seed_range: SeedRange) -> SeedRange:
        start = max(self.source_start, seed_range.start)
        end = min(self.source_end, seed_range.end)

        overlap = None

        if end > start:
            overlap = SeedRange(start, end - start)

        return overlap

    @property
    def translation(self) -> int:
        return self.dest_start - self.source_start

    def __call__(self, source_value) -> int:
        return source_value - self.source_start + self.dest_start


@dataclass
class Maps:
    maps: List[Map]

    @staticmethod
    def from_lines(lines: List[str]) -> Maps:
        maps = [Map(*map(int, line.split(" "))) for line in lines]
        return Maps(maps)

    @property
    def min_source_start(self):
        return min([m.source_start for m in self.maps])

    @property
    def max_source_end(self):
        return max([m.source_end for m in self.maps])

    def __call__(self, seed_range: SeedRange) -> List[SeedRange]:
        seed_ranges = []

        # Find overlap between seed range and the maps
        for map in self.maps:
            seed_range_overlap = map.overlap(seed_range)
            if seed_range_overlap is not None:
                seed_range_overlap.start += map.translation
                seed_ranges.append(seed_range_overlap)

        # Find non overlapping seed range at start
        if seed_range.start < self.min_source_start:
            seed_ranges.append(
                SeedRange(
                    seed_range.start,
                    min(seed_range.end, self.min_source_start) - seed_range.start,
                )
            )

        # Find non overlapping seed range at end
        if seed_range.end > self.max_source_end:
            s = max(seed_range.start, self.max_source_end)
            seed_ranges.append(SeedRange(s, seed_range.end - s))

        return seed_ranges


@dataclass
class Pipeline:
    seed_to_soil: Map
    soil_to_fertilizer: Map
    fertilizer_to_water: Map
    water_to_light: Map
    light_to_temp: Map
    temp_to_humidity: Map
    himidity_to_location: Map

    def __call__(self, seed_ranges) -> int:
        soils = []
        fertilizers = []
        waters = []
        lights = []
        temps = []
        humidities = []
        locations = []

        for seed_range in seed_ranges:
            soils += self.seed_to_soil(seed_range)

        for soil in soils:
            fertilizers += self.soil_to_fertilizer(soil)

        for fertilizer in fertilizers:
            waters += self.fertilizer_to_water(fertilizer)

        for water in waters:
            lights += self.water_to_light(water)

        for light in lights:
            temps += self.light_to_temp(light)

        for temp in temps:
            humidities += self.temp_to_humidity(temp)

        for humidity in humidities:
            locations += self.himidity_to_location(humidity)

        return locations


def parse_maps(inp: str) -> Tuple[List[int], Pipeline]:
    inp = [i.strip() for i in inp]
    seeds_list = list(map(int, (inp[0].split(": ")[-1].strip().split(" "))))

    seeds_ranges = []

    for i in range(0, len(seeds_list), 2):
        seeds_ranges.append(SeedRange(seeds_list[i], seeds_list[i + 1]))

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

    return seeds_ranges, Pipeline(
        seed_to_soil_maps,
        soil_to_fertilizer_maps,
        fertilizer_to_water_maps,
        water_to_light_maps,
        light_to_temp_maps,
        temp_to_humidity_maps,
        humidity_to_location_maps,
    )


def solve(inp: str) -> None:
    seed_ranges, pipeline = parse_maps(inp)

    output = min([s.start for s in pipeline(seed_ranges)])

    print(output)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
