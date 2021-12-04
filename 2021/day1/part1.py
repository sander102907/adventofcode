with open('input.txt') as f:
    measurements = f.read().split('\n')

output = sum([1 if int(measurements[i]) > int(measurements[i - 1]) else 0 for i in range(1, len(measurements))])
print(output)