def checksum(file_name):
    f = [x for x in open(file_name)]
    count_twos = 0
    count_threes = 0
    for x in f:
        q = dict()
        for a in set(x):
            if (x.count(a) == 2) :
                q[2] = x
            if (x.count(a) == 3):
                q[3] = x
        count_twos += int(2 in q)
        count_threes += int(3 in q)
    return count_twos * count_threes

def commonLetters(file_name):
    f = [x.strip() for x in open(file_name)]
    for fst in f:
        for snd in f:
            common_letters = []
            dist = 0
            for x in range(len(fst)):
                if fst[x] != snd[x]:
                    dist += 1
                else:
                    common_letters.append(fst[x])
            if dist == 1:
                return "".join(common_letters)


print("Day 2 - Part A: " + str(checksum("input.txt")))
print("Day 2 - Part B: " + str(commonLetters("input.txt")))
