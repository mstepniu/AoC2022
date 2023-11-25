input_stream = open("2022Day5.txt", "r")

data = input_stream.readlines()


# yes i loaded data manually.  and wanted to shoot myself halfway
# through it but was too far along to stop
stack1 = ["R", "N", "P", "G"]
stack2 = ["T", "J", "B", "L", "C", "S", "V", "H"]
stack3 = ["T", "D", "B", "M", "N", "L"]
stack4 = ["R", "V", "P", "S", "B"]
stack5 = ["G", "C", "Q", "S", "W", "M", "V", "H"]
stack6 = ["W", "Q", "S", "C", "D", "B", "J"]
stack7 = ["F", "Q", "L"]
stack8 = ["W", "M", "H", "T", "D", "L", "F", "V"]
stack9 = ["L", "P", "B", "V", "M", "J", "F"]

stack = list()
stack.append([])
stack.append(stack1)
stack.append(stack2)
stack.append(stack3)
stack.append(stack4)
stack.append(stack5)
stack.append(stack6)
stack.append(stack7)
stack.append(stack8)
stack.append(stack9)



for line in data:
    line = line.rstrip("\n")
    line = line.split(" ")
    if line[0] != "move":
        continue
    counter = int(line[1])
    f = int(line[3])
    t = int(line[5])
    for i in range(counter):
        stack[t].append(stack[f][len(stack[f])-1])
        stack[f].pop()

total = ""

for x in range(1, 10):
    total += stack[x][len(stack[x])-1]

print(total)

#part2
stack1 = ["R", "N", "P", "G"]
stack2 = ["T", "J", "B", "L", "C", "S", "V", "H"]
stack3 = ["T", "D", "B", "M", "N", "L"]
stack4 = ["R", "V", "P", "S", "B"]
stack5 = ["G", "C", "Q", "S", "W", "M", "V", "H"]
stack6 = ["W", "Q", "S", "C", "D", "B", "J"]
stack7 = ["F", "Q", "L"]
stack8 = ["W", "M", "H", "T", "D", "L", "F", "V"]
stack9 = ["L", "P", "B", "V", "M", "J", "F"]

stack = list()
stack.append([])
stack.append(stack1)
stack.append(stack2)
stack.append(stack3)
stack.append(stack4)
stack.append(stack5)
stack.append(stack6)
stack.append(stack7)
stack.append(stack8)
stack.append(stack9)


for line in data:
    line = line.rstrip("\n")
    line = line.split(" ")
    if line[0] != "move":
        continue
    counter = int(line[1])
    f = int(line[3])
    t = int(line[5])
    for i in range(counter, 0, -1):
        stack[t].append(stack[f][len(stack[f])-i])
    for i in range(counter):
        stack[f].pop()
total2 = ""

for x in range(1, 10):
    total2 += stack[x][len(stack[x])-1]

print(total2)

