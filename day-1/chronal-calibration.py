def resulting_freq(file_name):
    f = open(file_name)
    return sum([int(x) for x in list(f)])


def first_duplicate_freq(file_name):
    f = [int(x) for x in open(file_name)]
    cur_freq = 0
    seen_freq = set()
    idx = 0
    while(cur_freq not in seen_freq):
        seen_freq.add(cur_freq)
        cur_freq += f[idx]
        idx = (idx+1) % (len(f))
    return cur_freq


print("Day 1 - Part A: " + str(resulting_freq("input.txt")))
print("Day 1 - Part B: " + str(first_duplicate_freq("input.txt")))
