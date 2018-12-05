from collections import defaultdict

def load_guard_data(file_name):
    f = [x for x in open(file_name)]
    fs = sorted(f, key = lambda x: int(x[1:11].replace("-", "")+ x[13:17].replace(":","")))
    guard = defaultdict(lambda:[0 for x in range(60)])
    asleep = 0
    wake = 0
    g = ''
    for x in fs:
        if x[25] == "#":
            g = x.split()[3][1:]
        elif x[25] == "a":
            asleep = int(x[15:17])
        else:
            wake = int(x[15:17])
            for x in range(asleep, wake):
                guard[g][x] += 1
    return guard

def sleepy_guard(file_name):
    guard = load_guard_data(file_name)
    sleepiest = sorted(guard.keys(), key = lambda g: sum(guard[g]), reverse=True)[0]
    return (int(guard[sleepiest].index(max(guard[sleepiest]))) * int(sleepiest))

def most_sleepy(file_name):
    guard = load_guard_data(file_name)
    sleeeps_alot = sorted(guard.keys(), key = lambda g: max(guard[g]), reverse=True)[0]
    return (int(guard[sleeeps_alot].index(max(guard[sleeeps_alot]))) * int(sleeeps_alot))

print("Day 4 - Part A: " + str(sleepy_guard("input.txt")))
print("Day 4 - Part B: " + str(most_sleepy("input.txt")))
