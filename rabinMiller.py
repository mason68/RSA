import random

def rabinmiller(n, k):
    if n % 2 == 0:
        return False
    z = 0
    x = n - 1
    while True:
        quotient, remainder = divmod(x, 2)
        if remainder == 1:
            break
        z += 1
        x = quotient
    assert (2 ** z * x == n - 1)

    def comp(a):
        if pow(a, x, n) == 1:
            return False
        for i in range(z):
            if pow(a, 2 ** i * x, n) == n - 1:
                return False
        return True

    for i in range(k):
        a = random.randrange(2, n)
        if comp(a):
            return False

    return True

if rabinmiller(18946439013930052113248351940, 20):
    print("Definitely prime!")
else:
    print ("Composite!!")
