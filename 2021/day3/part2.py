with open('input.txt') as f:
    inputs = f.read().split('\n')


def bit_criteria(bits, bit_index, most_common):
    ones = sum([int(bit[bit_index]) for bit in bits])
    if most_common:
        return '1' if ones >= (len(bits)/2) else '0'
    else:
        return '0' if ones >= (len(bits)/2) else '1'

def find_rating(inputs, most_common=True):
    index = 0

    while(len(inputs) > 1):
        bit_criteria_value = bit_criteria(inputs, index, most_common)
        inputs = [i for i in inputs if i[index] == bit_criteria_value]

        index = (index + 1) % len(inputs[0])

    return inputs[0]

oxygen_rating = find_rating(inputs.copy())
co2_rating = find_rating(inputs.copy(), False)

print(int(oxygen_rating, 2) * int(co2_rating, 2))