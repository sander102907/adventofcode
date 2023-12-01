import os


def solve(calibration_document: str) -> None:
    """
    Print the sum of all of the calibration values
    """
    total = 0

    for s in calibration_document:
        # Get al numbers from string
        numbers = "".join(filter(lambda s: s.isnumeric(), s))
        # Get first and last digit only
        numbers = int(numbers[0] + numbers[-1])
        # Add to sum
        total += numbers
        
    print(total)

if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
