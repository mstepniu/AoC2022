#BRUTE FORCED for part1
#part2 needs to be clever
import timeit

with open("2022Day11.txt") as file:
    commands = file.readlines()

starting_items = list()
operations = list()
tests = list()
trues = list()
falses = list()
inspected = [0, 0, 0, 0, 0, 0, 0, 0]

for i in commands:
    i = i.strip()
    if i.startswith("Starting items"):
        temp = (i[16:].split(","))
        starting_items.append(list(map(int, temp)))
    elif i.startswith("Operation"):
        operations.append(i[21:])
    elif i.startswith("Test"):
        tests.append(int(i[19:]))
    elif i.startswith("If true"):
        trues.append(int(i[25:]))
    elif i.startswith("If false"):
        falses.append(int(i[26:]))
rounds = 1

workingvars = list()

#change this to 20 for part1
while rounds <= 10000:
    try:
        for m in range(8):
            #do each monkey
            for i in range(len(starting_items[m])):
                #do starting items of each monkey
                tempitem = starting_items[m].pop(0)
                inspected[m] += 1
                if operations[m] == "* old":
                    tempitem = tempitem * tempitem
                elif operations[m][0] == "*":
                    tempitem *= int(operations[m][2])
                elif operations[m][0] == "+":
                    tempitem += int(operations[m][2])
                #change this out for part1
                # tempitem = int(tempitem / 3)
                tempitem = int(tempitem) % 9699690

                if tempitem % tests[m] != 0:
                    starting_items[falses[m]].append(tempitem)
                else:
                    starting_items[trues[m]].append(tempitem)
    except IndexError as e:
        print(e)
    rounds += 1

#print(starting_items)
inspected.sort()
print(inspected[6] * inspected[7])

# 3,239,208,048,300,000 too high
#       323,920,804,830 too high
# 30893109657 correct answer?
