import os
from dataclasses import dataclass
from enum import Enum
from collections import Counter

class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OA_KIND = 4
    FULL_HOUSE = 5
    FOUR_OA_KIND = 6
    FIVE_OA_KIND = 7

@dataclass
class Hand:
    cards: str
    bid: int

    @property
    def type(self) -> Type:
        card_counts = sorted(list(Counter(self.cards).values()))

        if card_counts[-1] == 5:
            return Type.FIVE_OA_KIND
        if card_counts[-1] == 4:
            return Type.FOUR_OA_KIND
        if card_counts[-1] == 3 and card_counts[-2] == 2:
            return Type.FULL_HOUSE
        if card_counts[-1] == 3:
            return Type.THREE_OA_KIND
        if card_counts[-1] == 2 and card_counts[-2] == 2:
            return Type.TWO_PAIR
        if card_counts[-1] == 2:
            return Type.ONE_PAIR

        return Type.HIGH_CARD


def solve(lines: str) -> None:
    hands = [Hand(l.split(" ")[0], int(l.split(" ")[1])) for l in lines]

    # Sort the cards first
    card_values = "AKQJT98765432"
    hands.sort(key=lambda h: [card_values.index(c) for c in h.cards], reverse=True)    
    # Sort on card type
    hands.sort(key=lambda h: h.type.value)

    output = sum([(rank + 1) * h.bid for rank, h in enumerate(hands)])

    print(output)

if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
