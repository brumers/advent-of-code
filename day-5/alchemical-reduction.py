import re

def react(polymer):
    reaction = []
    for x in polymer:
        if len(reaction) == 0:
            reaction.append(x)
        else:
            a = reaction[-1]
            if (a.lower() == x.lower() and((a.isupper() and x.islower()) or (a.islower() and x.isupper()))):
                reaction.pop()
            else:
                reaction.append(x)
    return len(reaction)

def polymer_react(file_name):
    f = open(file_name).read().replace('\n', '')
    return react(f)

def poly_remove_react(file_name):
    f = open(file_name).read().replace('\n', '')
    uniq = []
    for x in set(f.lower()):
        src_str  = re.compile(x, re.IGNORECASE)
        str_replaced  = src_str.sub("",f)
        uniq.append(react(str_replaced))
    return min(uniq)

print("Day 5 - Part A: " + str(polymer_react("input.txt")))
print("Day 5 - Part B: " + str(poly_remove_react("input.txt")))
