import os
import math

def compute_amt_ways(total_t: int, distance_to_beat: int) -> int:
    dis = total_t**2 - 4 * distance_to_beat
    sqrt_val = math.sqrt(abs(dis))

    button_min_time = (-total_t + sqrt_val)/(2)
    button_max_time = (-total_t - sqrt_val)/(2)

    button_min_time = math.floor(abs(button_min_time) + 1)
    button_max_time = math.ceil(abs(button_max_time) - 1)

    return button_max_time - button_min_time + 1



def solve(lines: str) -> None:
    output = compute_amt_ways(51926890, 222203111261225)

    print(output)



if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
