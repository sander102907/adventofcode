with open('input.txt') as f:
    measurements = f.read().split('\n')

measurements = [int(m) for m in measurements]
output = 0

for i in range(1, len(measurements) - 2):
    first_group = measurements[i-1] + measurements[i] + measurements[i+1]
    second_group = measurements[i] + measurements[i+1] + measurements[i+2]

    if second_group > first_group:
        output += 1

print(output)