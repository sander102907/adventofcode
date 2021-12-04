with open('input.txt') as f:
    measurements = f.read().split('\n')

distance = 0
depth = 0

for m in measurements:
    move_size = int(m.split(" ")[-1])
    if "up" in m:
        depth -= move_size
    elif "down" in m:
        depth += move_size
    else:
        distance += move_size

print(distance * depth)