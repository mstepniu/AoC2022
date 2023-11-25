with open("2022Day9.txt") as file:
    commands = file.readlines()
from collections import defaultdict
positions = defaultdict(int)

head = [0,0]
tail = [0,0]

positions[(tail[0], tail[1])] = 0



def checktail():
    for i in range(10):
        pass
    if head[0] - tail[0] > 1:
        tail[0] += 1
        if tail[1] > head[1]:
            tail[1] -= 1
        elif tail[1] < head[1]:
            tail[1] += 1
    if tail[0] - head[0] > 1:
        tail[0] -= 1
        if tail[1] > head[1]:
            tail[1] -= 1
        elif tail[1] < head[1]:
            tail[1] += 1
    if head[1] - tail[1] > 1:
        tail[1] += 1
        if tail[0] < head[0]:
            tail[0] += 1
        elif tail[0] > head[0]:
            tail[0] -= 1
    if tail[1] - head[1] > 1:
        tail[1] -= 1
        if tail[0] < head[0]:
            tail[0] += 1
        elif tail[0] > head[0]:
            tail[0] -= 1
    positions[(tail[0], tail[1])] = 0

for i in commands:
    direction, steps = i.split()
    if direction == "D":
        for p in range(1, int(steps) + 1):
            head[1] -= 1
            checktail()
    elif direction == "U":
        for p in range(1, int(steps) + 1):
            head[1] += 1
            checktail()
    elif direction == "R":
        for p in range(1, int(steps) + 1):
            head[0] += 1
            checktail()
    else:
        for p in range(1, int(steps) + 1):
            head[0] -= 1
            checktail()

print(len(positions))

# 11584 too high
# 6324 too high
# 5862 too low

##PART2

snake = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]


positions.clear()
positions[(snake[9][0], snake[9][1])] = 0




def checktail():
    for i in range(9):
        if snake[i][0] - snake[i+1][0] > 1:
            snake[i+1][0] += 1
            if snake[i+1][1] > snake[i][1]:
                snake[i+1][1] -= 1
            elif snake[i+1][1] < snake[i][1]:
                snake[i+1][1] += 1
        if snake[i+1][0] - snake[i][0] > 1:
            snake[i+1][0] -= 1
            if snake[i+1][1] > snake[i][1]:
                snake[i+1][1] -= 1
            elif snake[i+1][1] < snake[i][1]:
                snake[i+1][1] += 1
        if snake[i][1] - snake[i+1][1] > 1:
            snake[i+1][1] += 1
            if snake[i+1][0] < snake[i][0]:
                snake[i+1][0] += 1
            elif snake[i+1][0] > snake[i][0]:
                snake[i+1][0] -= 1
        if snake[i+1][1] - snake[i][1] > 1:
            snake[i+1][1] -= 1
            if snake[i+1][0] < snake[i][0]:
                snake[i+1][0] += 1
            elif snake[i+1][0] > snake[i][0]:
                snake[i+1][0] -= 1
        positions[(snake[9][0], snake[9][1])] = 0
for i in (commands):
    direction, steps = i.split()
    if direction == "D":
        for p in range(1, int(steps) + 1):
            snake[0][1] -= 1
            checktail()
    elif direction == "U":
        for p in range(1, int(steps) + 1):
            snake[0][1] += 1
            checktail()
    elif direction == "R":
        for p in range(1, int(steps) + 1):
            snake[0][0] += 1
            checktail()
    else:
        for p in range(1, int(steps) + 1):
            snake[0][0] -= 1
            checktail()

print(len(positions))