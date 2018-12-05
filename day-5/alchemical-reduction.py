def polymer_react(file_name):
    f = open(file_name).read().replace('\n', '')
    print(len(f))
    reaction = []
    for x in f:
        if len(reaction) == 0:
            reaction.append(x)
        else:
            a = reaction[-1]
            if (a.lower() == x.lower() and((a.isupper() and x.islower()) or (a.islower() and x.isupper()))):
                reaction.pop()
            else:
                reaction.append(x)
    return len(reaction)

print(str(polymer_react("input.txt")))
