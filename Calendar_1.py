fobj = open('frequencies.txt', 'r')
freq_liste = [int(x.strip('\n ')) for x in fobj]

freq = 0
frequencies = [0]

print freq in frequencies




def findfreq(freq_list):
    freq = 0
    frequencies = [0]
    for j in range(1000):
        for i in freq_list:
            freq += i
            if freq in frequencies:
                return freq, j
            frequencies.append(freq)


print findfreq(freq_liste)
