from collections import defaultdict

def largest_area(file_name):
    f = [x for x in open(file_name)]

    cords = defaultdict()
    for idx, x in enumerate(f):
        cords[idx] = (int(x.split()[0][:-1]),int(x.split()[1]))
    max_x = sorted([y[0] for x,y in cords.items()])[-1]
    max_y = sorted([y[1] for x,y in cords.items()])[-1]
    maxX = max(max_x, max_y)
    grid = [[0 for x in range(maxX)] for y in range(maxX)]

    counts = defaultdict(lambda : 0)
    safe_count = 0
    for y in range(0, maxX):
        for x in range(0, maxX):
            dists = defaultdict(list)
            totalDist = 0
            for id, c in cords.items():
                d = abs(c[0] - x) + abs(c[1] - y)
                totalDist += d
                dists[d].append(id)
            if(totalDist < 10000):
                safe_count += 1
            (hf, hg) = sorted( [(a,b) for (a,b) in dists.items()], key= lambda (a,b) : a )[0]
            if len(hg) == 1:
                grid[y][x] =  str(hg[0])
                counts[str(hg[0])] += 1
            else:
                grid[y][x] = '.'
    edges = set()
    for a in range(0, maxX):
        edges.add(grid[a][0])
        edges.add(grid[0][a])
        edges.add(grid[a][maxX-1])
        edges.add(grid[maxX-1][a])
    edges.discard('.')
    for e in edges: counts.pop(e)
    return (sorted([(x,y) for (x,y) in counts.items()], key = lambda (a, b) : b, reverse = True)[0][1], safe_count)

print(largest_area("input.txt"))
