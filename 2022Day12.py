# https://adventofcode.com/2022/day/12

with open("2022Day12.txt", 'r') as file:
    data = [[l for l in line] for line in file.read().strip().split()]

# go through the data and set the starting point to "a" and the endpoint
# to "{" which is greater than "z" when doing comparisons.  "{" > "z"
# "{" = z + 1

for i in range(len(data)):
    if "S" in data[i]:
        data[i][data[i].index("S")] = "a"
    if "E" in data[i]:
        data[i][data[i].index("E")] = "{"

#define dictionaries
# visited used to keep track if i've been that that node before
visited = dict()
#part1path is to keep track of the steps taken to get to each node
part1path = dict()
#part2path is the same as part1 except when we encounter "a" we set steps to 0
part2path = dict()

#initialize dictionaries and lists
part1path[(20, 0)] = 0
part2path[(20, 0)] = 0
#nextnode is used to for evaluating the adjacent nodes
nextnode = list()
nextnode.append((20, 0))
#i manually put the starting position in each but it could easily of been
#programmed as a variable


#checks if x coordinate is out of upper bounds
def checkup(x):
    return True if x + 1 <= len(data)-1 else False


#checks if x coordinate is out of lower bounds
def checkdown(x):
    return True if x - 1 >= 0 else False


#checks if y coordinate is out of right upper bounds
def checkright(y):
    return True if y + 1 <= len(data[0])-1 else False


#checks if y coordinate is out of left lower bounds
def checkleft(y):
    return True if y - 1 >= 0 else False

#keep looping as long as there is another node to check in the list
while True:
    #i'm checking if we ever get to the end node and if so break the loop
    if len(nextnode) > 0:
        p = nextnode[0][0]
        q = nextnode[0][1]
        if data[p][q] == "{":
            #print("Loop broken because E found")
            break
    else:
        #this was for testing purposes.  If there are no more nodes to check
        #and we havent found the endpoint, something went wrong...
        print("Nextnode Empty")
        break
    #get the next node to check
    checknext = nextnode.pop(0)

    #if we have visited this node before.. skip
    if checknext in visited:
        continue
    #we haven't visited the node yet but are going to visit now, so add it to visited.
    visited[checknext] = 1

    #break up the node into x and y coordinates
    x = checknext[0]
    y = checknext[1]

    #checks if x is out of bounds
    if checkup(x):
        #checks if the current location letter + 1, is equal to or lower than adjacent letter
        if data[x+1][y] <= chr(ord(data[x][y]) + 1):
            #now we make sure it's not in the nextnode list to be processed already
            if (x+1, y) not in nextnode:
                #add it to the queue of items to be processed
                nextnode.append((x+1, y))
                #we make sure it's not already been previously counted in the path
                if (x+1, y) not in part1path:
                    #part1 we take the count from [x,y].  add 1 step and assign to adjacent node
                    part1path[(x + 1, y)] = part1path[(x, y)] + 1
                    #part2 said to move around until the nearest base "a" is found to start counting
                    if data[x+1][y] == "a":
                        #we reset the steps to 0 if we find an "a"
                        part2path[(x + 1, y)] = 0
                    #didn't find an "a" so add a step
                    else:
                        part2path[(x + 1, y)] = part2path[(x, y)] + 1

    if checkdown(x):
        if data[x-1][y] <= chr(ord(data[x][y]) + 1):
            if (x-1, y) not in nextnode:
                nextnode.append((x-1, y))
                if (x-1, y) not in part1path:
                    part1path[(x - 1, y)] = part1path[(x, y)] + 1
                if data[x - 1][y] == "a":
                    part2path[(x - 1, y)] = 0
                else:
                    part2path[(x - 1, y)] = part2path[(x, y)] + 1

    if checkright(y):
        if data[x][y+1] <= chr(ord(data[x][y]) + 1):
            if (x, y+1) not in nextnode:
                nextnode.append((x, y+1))
                if (x, y+1) not in part1path:
                    part1path[(x, y + 1)] = part1path[(x, y)] + 1
                if data[x][y+1] == "a":
                    part2path[(x, y+1)] = 0
                else:
                    part2path[(x, y+1)] = part2path[(x, y)] + 1

    if checkleft(y):
        if data[x][y-1] <= chr(ord(data[x][y]) + 1):
            if (x, y-1) not in nextnode:
                nextnode.append((x, y-1))
                if (x, y-1) not in part1path:
                    part1path[(x, y - 1)] = part1path[(x, y)] + 1
                if data[x][y-1] == "a":
                    part2path[(x, y-1)] = 0
                else:
                    part2path[(x, y-1)] = part2path[(x, y)] + 1


#could have easily used variables instead of hardcoding but alas...
print(part1path[(20, 88)])
print(part2path[(20, 88)])
