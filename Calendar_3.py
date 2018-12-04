fobj = open('text.txt')

data = [x.strip('\n') for x in fobj]

testdata = '#1 @ 287,428: 27x20\n #2 @ 282,539: 20x10\n #3 @ 550,118: 20x23\n #4 @ 454,774: 20x19\n #5 @ 542,157: 11x24'
datadata = testdata.split('\n ')

grid = [[0 for x in range(1000)] for y in range(1000)]
summ = 0
usedid = []
ids = []
for line in data:
    identifier = int(line.split('@')[0].strip('# '))
    ids.append(identifier)
    startx = int(line.split(',')[0].split('@')[1].strip())
    starty = int(line.split(',')[1].split(':')[0].strip())
    x = int(line.split('x')[0].split(':')[1].strip())
    y = int(line.split('x')[1])

    for i in range(startx, startx + x):
        for j in range(starty, starty + y):
            if grid[i][j] == 0:
                grid[i][j] = identifier

            elif grid[i][j] == 'X':
                usedid.append(identifier)
            else:
                usedid.append(identifier)
                usedid.append(grid[i][j])
                grid[i][j] = 'X'
                summ += 1
print summ
print str(set(ids)-set(usedid)).strip('set([])')