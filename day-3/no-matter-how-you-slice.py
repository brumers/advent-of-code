def parse_file(file_name):
    f = [x for x in open(file_name)]
    material = [[0 for x in range(1000)] for y in range(1000)]
    claims = []
    for x in f:
        id, sep, c, s = x.split()
        cord = [int(x) for x in c[:-1].split(",")]
        size = [int(x) for x in s.split("x")]
        for a in range(cord[0], cord[0] + size[0]):
            for y in range(cord[1], cord[1] + size[1]):
                material[a][y] = material[a][y] + 1
                claims.append((id, cord, size))
    return (material, claims)

def multi_claims(file_name):
    material, _ = parse_file(file_name)
    multi = 0
    for x in material:
        for y in x:
            if y > 1:
                multi = multi + 1
    return multi

def intact_claim(file_name):
    material, claims = parse_file(file_name)
    for (id, cord, size) in claims:
        found = True
        for x in range(cord[0], cord[0] + size[0]):
            for y in range(cord[1], cord[1] + size[1]):
                found = found and (material[x][y] == 1)
        if found : return id
    return -1

print("Day 3 - Part A: " + str(multi_claims('input.txt')))
print("Day 3 - Part B: " + str(intact_claim('input.txt')))
