fobj = open('Calendar_3_in.txt', 'r')

data = [x for x in fobj]

data.sort()
dates = []
is1021 = []
for i in range(len(data)):
    data[i] = data[i][12:]
    if '#' in data[i]:
        if i > 0:
            dates.append(newData)
        newData = [int(data[i][data[i].find('#') + 1: data[i].find('b') - 1])]

    else:
        newData.append(int(data[i][3:5]))


asleep = {}
times = {}
for i in range(len(dates)):
    while len(dates[i]) > 2:
        aw = dates[i].pop()
        asl = dates[i].pop()
        if dates[i][0] == 1021:
            is1021.append([asl, aw])
        if dates[i][0] in asleep:
            asleep[dates[i][0]] = asleep[dates[i][0]] + aw - asl
        else:
            asleep[dates[i][0]] = aw - asl
        if dates[i][0] in times:
            times[dates[i][0]].append([asl, aw])
        else:
            times[dates[i][0]] = [[asl, aw]]

results = {}
for key in times.keys():

    hour = [0 for i in range(60)]

    for i in range(len(times[key])):
        for j in range(times[key][i][0], times[key][i][1]):
            hour[j] += 1
    number = max(hour)
    minute = hour.index(max(hour))
    results[number] = [minute, key]

solution2 = results[max(results.keys())][0]*results[max(results.keys())][1]
print solution2

solution1 = hour.index(max(hour))* asleep.keys()[asleep.values().index(max(asleep.values()))]
print solution1

