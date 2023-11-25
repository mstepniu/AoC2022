with open("2022Day8.txt") as file:
    commands = file.readlines()

topmax = list()
botmax = list()
leftmax = list()
rightmax = list()

treecounter = 0

for i in commands[0]:
    topmax.append(i)
for i in commands[98]:
    botmax.append(i)
for i in range(len(commands)):
    leftmax.append(commands[i][0])
    rightmax.append(commands[i][98])

visibleflag = True
visibletree = 0

rightflag = True
topflag = True
leftflag = True
bottomflag = True
scenictop = 0
scenicbot = 0
scenicleft = 0
scenicright = 0

scenicfinal = 0

for x in range(99):
    for y in range(99):
        # check right of number
        for yy in range(y+1, 99):
            scenicright += 1
            if int(commands[x][y]) < int(commands[x][yy]) + 1:
                rightflag = False
                break
        # check left of number
        for yy in range(y-1, -1, -1):
            scenicleft += 1
            if int(commands[x][y]) < int(commands[x][yy]) + 1:
                leftflag = False
                break
        # check below number
        for xx in range(x-1, -1, -1):
            scenicbot += 1
            if int(commands[x][y]) < int(commands[xx][y]) + 1:
                bottomflag = False
                break
        # check above number
        for xx in range(x+1, 99):
            scenictop += 1
            if int(commands[x][y]) < int(commands[xx][y]) + 1:
                topflag = False
                break

        if leftflag == True or topflag == True or rightflag == True or bottomflag == True:
            visibletree += 1

        rightflag = True
        leftflag = True
        topflag = True
        bottomflag = True
        if scenictop == 0:
            scenictop = 1
        if scenicbot == 0:
            scenicbot = 1
        if scenicright == 0:
            scenicright = 1
        if scenicleft == 0:
            scenicleft = 1
        if (scenicbot * scenicright * scenicleft * scenictop) > scenicfinal:
            scenicfinal = scenicbot * scenicright * scenicleft * scenictop

        if scenicfinal > 1500000:
            print("x: ", x)
            print("y: ", y)
            print(commands[x][y])
            print(commands[x][y-1])
            print(commands[x])
            print("Bot: ", scenicbot)
            print("Left: ", scenicleft)
            print("Top: ", scenictop)
            print("Right: ", scenicright)
        scenicright = 0
        scenicleft = 0
        scenictop = 0
        scenicbot = 0

print(visibletree)
print(scenicfinal)