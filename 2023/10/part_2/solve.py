import os
from typing import List
from dataclasses import dataclass
from shapely.geometry import Polygon


@dataclass
class Node:
    char: str
    row: int
    column: int
    next: "Node"

    def __eq__(self, other):
        if isinstance(other, Node):
            return (
                self.char == other.char
                and self.row == other.row
                and self.column == other.column
            )
        return False


locations = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

allowed_connections = {
    "N": ["F", "|", "7", "S"],
    "E": ["J", "-", "7", "S"],
    "S": ["L", "|", "J", "S"],
    "W": ["F", "-", "L", "S"],
}


directions_to_check = {
    "S": ["N", "E", "S", "W"],
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["W", "S"],
    "F": ["S", "E"],
    ".": [],
}


def find_edges(start_node: Node, grid: List[List[str]], all_nodes):
    queue = [start_node]

    for node in queue:
        directions = directions_to_check[node.char]

        for direction in directions:
            cell = locations[direction]
            row = cell[0]
            column = cell[1]

            row_index = node.row + row

            # Skip when row out of range
            if row_index < 0 or row_index > len(grid) - 1:
                continue

            # Column to check
            column_index = node.column + column

            # Skip when column out of range
            if column_index < 0 or column_index > len(grid[row_index]) - 1:
                continue

            # Not visited yet
            if all_nodes[row_index][column_index] is None:
                # Find char
                neigbour_character = grid[row_index][column_index]

                # Check if char is in allowed connections
                if neigbour_character in allowed_connections[direction]:
                    # Next node
                    target_node = add_node(
                        node, neigbour_character, row_index, column_index, all_nodes
                    )
                    queue.append(target_node)
                    break

            # If we arrive back at the start node (after at least three)
            if all_nodes[row_index][column_index] == start_node and len(queue) > 3:
                node.next = start_node
                break


def add_node(node: Node, char: str, row: int, column: int, all_nodes):
    target_node = all_nodes[row][column]

    if target_node is None:
        new_node = Node(char, row, column, None)
        target_node = new_node
        all_nodes[row][column] = target_node

    if node.next is None or node.next == target_node:
        node.next = target_node
    else:
        print(
            f"Error: edges for node {node.char} at index {node.row},{node.column} already set."
        )

    return target_node


def find_max_distance(starting_node: Node):
    node = starting_node.next
    count = 1

    while node != starting_node:
        count += 1
        node = node.next

    return round(count / 2.0)


def solve(lines: str) -> None:
    grid = []
    for line in lines:
        grid.append(list(line.strip()))

    all_nodes = []
    for i, _ in enumerate(grid):
        all_nodes.append([])
        for j, _ in enumerate(grid[i]):
            all_nodes[i].append(None)
            if grid[i][j] == "S":
                start_pos = (i, j)

    starting_node = Node("S", start_pos[0], start_pos[1], None)
    all_nodes[start_pos[0]][start_pos[1]] = starting_node

    find_edges(starting_node, grid, all_nodes)

    coordinates = [(starting_node.row, starting_node.column)]

    current_node = starting_node.next
    num_nodes_in_path = 1

    while current_node is not starting_node:
        coordinates.append((current_node.row, current_node.column))
        current_node = current_node.next
        num_nodes_in_path += 1

    polygon = Polygon(coordinates)
    print(polygon.area - num_nodes_in_path / 2 + 1)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
