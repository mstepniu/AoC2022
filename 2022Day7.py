import sys
input_stream = open("2022Day7.txt", "r")
from collections import defaultdict

data = input_stream.readlines()


# dont record "dir <name>" command
# dict based on size and who size is associated with


location = list()
sums = defaultdict(int)
total2 = 0
for line in data:
    fields = line.split()
    #print(fields[0]+fields[1])
    if fields[0]+ " " + fields[1] == "$ ls" or fields[0] == "dir":
        continue
    elif len(fields) == 2:
        total2 += len(location)
        for i in location:
            sums[i] += int(fields[0])
    elif fields[2] == "..":
        location.pop()
    else:
        path = f"{location[-1]}_{fields[2]}" if location else fields[2]
        location.append(path)

total = 0


for i in sums:
    if sums[i] <= 100000:
        total += sums[i]

print(total)

#part2

targetsize = 30000000 - (70000000 - sums["/"])

for lowest in sorted(sums.values()):
    if lowest > targetsize:
        break

print(lowest)