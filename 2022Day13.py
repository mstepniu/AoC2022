# https://adventofcode.com/2022/day/13

import re

with open("2022Day13.txt", 'r') as file:
    data = file.read().strip().split()


def parser(s1):
    nodes = list()
    numbuilder = ""
    islist = list()
    listbuilder = list()

    for i in range(len(s1)):
        if s1[i] == "[":
            if len(islist) == 0:
                if numbuilder != "":
                    nodes.append(numbuilder[:])
            else:
                if len(listbuilder) != 0:
                    nodes.append(listbuilder[:])
            numbuilder = ""
            listbuilder.clear()
            islist.append(True)
        elif s1[i] == "]":
            if len(islist) == 0:
                if numbuilder != "":
                    nodes.append(numbuilder[:])
                else:
                    nodes.append(-1)
            else:
                if numbuilder != 0:
                    listbuilder.append(numbuilder)
                nodes.append(listbuilder[:])
            islist.pop()
            numbuilder = ""
            listbuilder.clear()
        elif s1[i].isnumeric():
            if numbuilder == "":
                numbuilder = s1[i]
            else:
                numbuilder += s1[i]
                if len(islist) == 0:
                    nodes.append(numbuilder[:])
                else:
                    listbuilder.append(numbuilder[:])
                numbuilder = ""
        elif s1[i] == ",":
            if numbuilder != "":
                if len(islist) == 0:
                    nodes.append(numbuilder[:])
                else:
                    listbuilder.append(numbuilder[:])
            numbuilder = ""
    return nodes


def compare(s1, s2):
    while len(s1) > 0 and len(s2) > 0:
        l = s1.pop(0)
        r = s2.pop(0)
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return 1
            elif l > r:
                return -1
        if isinstance(l, list) and isinstance(r, list):
            keep = compare(l, r)
            if keep != 0:
                return keep
        if isinstance(l, int) and isinstance(r, list):
            keep = compare(list([l]), r)
            if keep != 0:
                return keep
        if isinstance(l, list) and isinstance(r, int):
            keep = compare(l, list([r]))
            if keep != 0:
                return keep
    if len(s1) < len(s2):
        return 1
    elif len(s1) > len(s2):
        return -1
    else:
        return 0


count = 1
total = 0
totals = list()
for i in range(0, len(data)-1, 2):
    if compare(eval(data[i]), eval(data[i+1])) == 1:
        total += count
        totals.append(count)
    count += 1


print(sum(totals))
print(totals)

# 5100 - too low
# 5094 - wrong
# 5202 - wrong