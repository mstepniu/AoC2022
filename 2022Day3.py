input_stream = open("2022Day3.txt", "r")

data = input_stream.readlines()

total = 0


def value(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

for line in data:
    line = line.rstrip("\n")
    s = int(len(line) / 2)
    comp1 = line[:s]
    comp2 = line[s:]
    for i in comp1:
        if i in comp2:
            total += value(i)
            break
print(total)

elf = list()
counter = 0
total2 = 0

for line in data:
    line = line.rstrip("\n")
    if counter == 3:
        for i in elf[0]:
            if i in elf[1] and i in elf[2]:
                total2 += value(i)
                break
        elf.clear()
        elf.append(line)
        counter = 1
    else:
        elf.append(line)
        counter += 1


for i in elf[0]:
    if i in elf[1] and i in elf[2]:
        total2 += value(i)
        break
print(total2)