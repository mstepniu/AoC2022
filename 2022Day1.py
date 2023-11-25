# https://adventofcode.com/2022/day/1

input_stream = open("2022Day1.txt", "r")

data = input_stream.readlines()

totals = [0]

counter = 0
for line in data:
    if line == "\n":
        counter += 1
        totals.append(0)
    else:
        totals[counter] += int(line)

totals.sort()
print(totals[len(totals) - 1])

#part2
print(totals[len(totals) - 1] + totals[len(totals) - 2] + totals[len(totals) - 3])
