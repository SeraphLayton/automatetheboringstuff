import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    c = 0
    hs = 0
    randomlist = []
    for i in range(0,100):
        n = random.randint(0,1)
        if n == 1:
            randomlist.append('H')
        else:
            randomlist.append('T')
    for i in range(len(randomlist)):
        if randomlist[i] == 'H':
            c += 1
            if c == 6:
                hs += 1
                c = 0
        else:
            c = 0
    numberOfStreaks = numberOfStreaks + hs
print('Chance of streak: %s%%' % (numberOfStreaks / 100))