input_stream = open("2022Day4.txt", "r")

data = input_stream.readlines()

# each section has a uniq id
# each elf is assigned a range of section ids

# assignments overlap

total = 0

for line in data:
    elf1, elf2 = line.split(",")
    elf11, elf12 = elf1.split("-")
    elf21, elf22 = elf2.split("-")
    elf11 = int(elf11)
    elf12 = int(elf12)
    elf21 = int(elf21)
    elf22 = int(elf22)

    if elf11 <= elf21 and elf12 >= elf22:
        total += 1
    elif elf11 >= elf21 and elf12 <= elf22:
        total += 1
    else:
        pass

print(total)

total2 = 0
for line in data:
    elf1, elf2 = line.split(",")
    elf11, elf12 = elf1.split("-")
    elf21, elf22 = elf2.split("-")
    elf11 = int(elf11)
    elf12 = int(elf12)
    elf21 = int(elf21)
    elf22 = int(elf22)

    if elf21 <= elf11 <= elf22:
        total2 += 1
    elif elf21 <= elf12 <= elf22:
        total2 += 1
    elif elf11 <= elf21 <= elf12:
        total2 += 1
    elif elf11 <= elf22 <= elf12:
        total2 += 1
    else:
        pass

print(total2)