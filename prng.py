import random
from rabinMiller import rabinmiller

aa = 10000
for i in range(aa):
    p = 6571
    q = 7907
    n = p * q
    x = []
    y = []
    def bbs(c):
        d = random.randrange(1,10000000000)
        g = 0
        for i in list(range(c)):
            while g == 0:
                x.append(d**2 % n)
                g = 1
            x.append(x[i]**2 % n)

        for i in list(range(c)):
            y.append(x[i]%2)

    bbs(48)
    z = ''.join(map(str, y))
    zz = int(z, 2)
    print(zz)

    if rabinmiller(zz, 20):
        print("Definitely prime!")
        break
    else:
        print ("Composite!!")