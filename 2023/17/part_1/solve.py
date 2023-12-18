from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List, Tuple
import numpy as np


@dataclass
class Node:
    position: Tuple[int, int]
    value: int
    same_dir_counter: {}
    prev_dir: int
    p1: Node
    p2: Node
    p3: Node

    def next_nodes(self, map) -> List[Node]:
        rows, cols = len(map), len(map[0])
        # Define directions: 0 (left), 1 (down), 2 (right), 3 (up)
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        next_nodes = []

        for i, dir in enumerate(directions):
            new_same_dir_counter = 1
            new_row = self.position[0] + dir[0]
            new_col = self.position[1] + dir[1]

            if self.prev_dir == i:
                new_same_dir_counter = self.same_dir_counter + 1

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and (
                    not (
                        directions[self.prev_dir][0] * -1 == directions[i][0]
                        and directions[self.prev_dir][1] * -1 == directions[i][1]
                    )
                )
                and new_same_dir_counter <= 3
            ):
                next_nodes.append(
                    Node(
                        (new_row, new_col),
                        self.value + map[new_row][new_col],
                        new_same_dir_counter,
                        i,
                        self,
                        self.p1,
                        self.p2,
                    )
                )

        return next_nodes


def dijkstra(map):
    rows, cols = len(map), len(map[0])
    distances = np.full((rows, cols, 4, 3), fill_value=np.inf, dtype=float)
    distances[0, 1, 2] = map[0][1]
    distances[1, 0, 1] = map[1][0]

    start = Node(
        position=(0, 0),
        value=map[0][0],
        same_dir_counter=0,
        prev_dir=-1,
        p1=None,
        p2=None,
        p3=None,
    )

    second = Node(
        position=(0, 1),
        value=map[0][1],
        same_dir_counter=1,
        prev_dir=2,
        p1=start,
        p2=None,
        p3=None,
    )

    third = Node(
        position=(1, 0),
        value=map[1][0],
        same_dir_counter=1,
        prev_dir=1,
        p1=start,
        p2=None,
        p3=None,
    )

    unvisited_nodes = [second, third]

    while unvisited_nodes:
        node = min(unvisited_nodes, key=lambda node: node.value)

        # Remove the current node from the list of unvisited nodes
        unvisited_nodes.remove(node)

        # Explore neighbors in different directions
        for next_node in node.next_nodes(map):
            # Update distance if a shorter path is found
            if (
                next_node.value
                < distances[
                    next_node.position[0],
                    next_node.position[1],
                    next_node.prev_dir,
                    next_node.same_dir_counter - 1,
                ]
            ):
                distances[
                    next_node.position[0],
                    next_node.position[1],
                    next_node.prev_dir,
                    next_node.same_dir_counter - 1,
                ] = next_node.value
                unvisited_nodes.append(next_node)

    return np.min(distances[rows - 1, cols - 1])


def solve(lines: str) -> None:
    city_map = []

    for line in lines:
        row = []
        for number in line.strip():
            row.append(int(number))

        city_map.append(row)

    heat_loss = dijkstra(city_map)
    print(heat_loss)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
