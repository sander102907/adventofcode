import os

import heapq

def min_heat_loss(city_map):
    rows, cols = len(city_map), len(city_map[0])

    # Priority queue to store (heat loss, row, col, direction, consecutive_blocks) tuples
    pq = [(city_map[0][0], 0, 0, 0, 0)]

    # Set to keep track of visited positions, directions, and consecutive blocks
    visited = set()

    # Define directions: right, down, left, up (clockwise)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        heat_loss, i, j, k, c = heapq.heappop(pq)

        # Check if the destination is reached
        if i == rows - 1 and j == cols - 1:
            return heat_loss

        # Check if the current state has already been visited
        if (i, j, k) in visited:
            continue

        # Mark the current state as visited
        visited.add((i, j, k))

        # Try all possible directions
        for d in range(4):
            # Back is not allowed
            if directions[k][0] * -1 == directions[d][0] and directions[k][1] * -1 == directions[d][1]:
                continue

            ni, nj = i + directions[d][0], j + directions[d][1]

            # Check if the new position is within bounds
            if 0 <= ni < rows and 0 <= nj < cols:
                # Update the heat loss for the new position, direction, and consecutive blocks
                new_heat_loss = heat_loss + city_map[ni][nj]

                if d == k:
                    new_c = c + 1
                else:
                    new_c = 1

                # Check if consecutive blocks limit is not exceeded
                if new_c <= 3:
                    heapq.heappush(pq, (new_heat_loss, ni, nj, d, new_c))

    return float('inf')  # No path found

def solve(lines: str) -> None:
    city_map = []
    for line in lines:
        row = []
        for number in line.strip():
            row.append(int(number))
        
        city_map.append(row)

    result = min_heat_loss(city_map) - city_map[0][0]
    print("Minimum heat loss:", result)
    

if __name__ == "__main__":
    input_file = "sample_input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
