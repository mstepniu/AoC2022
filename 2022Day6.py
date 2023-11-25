input_stream = open("2022Day6.txt", "r")

data = input_stream.readline()

# start of packet = sequence of 4 characters that are all different
# report size from beginning of last of 4 characters (index of last char) + 1

rolling = list()
count = 0
for char in data:
    if len(rolling) < 14:
        count += 1
        rolling.append(char)
    if len(rolling) == 14:
        try:
            for i in rolling:
                temp = rolling.index(i)
                if i in rolling[temp+1:]:
                    #print(i, rolling[temp:], rolling)
                    rolling.pop(0)
                    break
                else:
                    #
                    print(count, "FINISHED")

        except ValueError as e:
            pass
print(rolling)