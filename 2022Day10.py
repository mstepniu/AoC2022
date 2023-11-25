with open("2022Day10.txt") as file:
    commands = file.readlines()


x = 1

count = 1

delay = list()

cycleflags = [False, False, False, False, False, False]
sums = 0
holdamt = 0

output = list()

cycle = -1

def checkpixel(cycle):
    if cycle >= 39:
        cycle -= 40
    if x+1 >= cycle and x-1 <= cycle:
        output.append("#")
    else:
        output.append(".")
    return cycle

for i in commands:
    cycle += 1
    cycle = checkpixel(cycle)
    count += 1
    if count >= 20 and cycleflags[0] is False:
        sums = (20 * x)
        cycleflags[0] = True
    if count >= 60 and cycleflags[1] is False:
        sums += (60 * x)
        cycleflags[1] = True
    if count >= 100 and cycleflags[2] is False:
        sums += (100 * x)
        cycleflags[2] = True
    if count >= 140 and cycleflags[3] is False:
        sums += (140 * x)
        cycleflags[3] = True
    if count >= 180 and cycleflags[4] is False:
        sums += (180 * x)
        cycleflags[4] = True
    if count >= 220 and cycleflags[5] is False:
        sums += (220 * x)
        cycleflags[5] = True

    if not i.startswith("noop"):
        cycle += 1
        cycle = checkpixel(cycle)
        instruction, amt = i.split()
        count += 1
        x += int(amt)

print(sums)

# 427040 too high
# 14300 too low
# 15020 too high
# 13140

print(*output[0:40], sep='')
print(*output[40:80], sep='')
print(*output[80:120], sep='')
print(*output[120:160], sep='')
print(*output[160:200], sep='')
print(*output[200:240], sep='')