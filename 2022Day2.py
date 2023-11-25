# A, X = Rock            A>Z  B>X  C>Y
# B, Y = Paper
# C, Z = Scissors


input_stream = open("2022Day2.txt", "r")

data = input_stream.readlines()

total = 0
total2 = 0

def changenum(let):
    if let == "A" or let == "X":
        return 1
    elif let == "B" or let == "Y":
        return 2
    elif let == "C" or let == "Z":
        return 3
    else:
        print("Error")

for line in data:
    player1, player2 = line.split()

    play1 = changenum(player1)
    play2 = changenum(player2)

    if (play1 == 2 and play2 == 3) or \
        (play1 == 3 and play2 == 1) or \
        (play1 == 1 and play2 == 2):
        total += play2 + 6
    elif play1 == play2:
        total += 3 + play2
    else:
        total += play2

    #part2
    if play2 == 2:      # draw
        total2 += (3 + play1)
    elif play2 == 1:    # lose
        if play1 == 1:
            total2 += 3
        else:
            total2 += ((play1 % 2) + 1)
    elif play2 == 3:               # win
        total2 += (7 + (play1 % 3))
    else:
        print("Error")
print(total)

print(total2)
