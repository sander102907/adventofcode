with open('input.txt') as f:
    inputs = f.read().split('\n')

most_common_binary = ""
least_common_binary = ""

for i in range(len(inputs[0])):
    ones = sum([int(x[i]) for x in inputs])
    
    if ones > (len(inputs)/2):
        most_common_binary += "1"
        least_common_binary += "0"
    else:
        most_common_binary += "0"
        least_common_binary += "1"

print(int(most_common_binary, 2) * int(least_common_binary, 2))
