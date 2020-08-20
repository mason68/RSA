
def rsa(p, q):
    rsa.e = 65537
    rsa.n = p * q
    totient = (p - 1) * (q - 1)

    #leaving this in, originally computed e
    #print("totient is" + str(totient))
    #print("n is "+ str(rsa.n))

    ###########  find e  ############
    #z = 65537 #change to e
    #z = 0 change all future z references to z-1
    #while e<50000:
    #    if math.gcd(z, totient) == 1:
    #        print(str(z) + " is relatively prime with " + str(totient))
    #        z = z + 1
    #        e = e + 1
    #    else:
    #        z = z + 1
    #        continue
    return totient

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def inverse(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

'''
c = rsa(256857627185587, 101793246072139)
a = inverse(rsa.e, c)

print("e = " + str(rsa.e) + " -- d = " + (hex(a)) + " -- n = " + hex(rsa.n))
'''



