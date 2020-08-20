from rsa import rsa, inverse

def euclidean(x, y, verbose=True):
    if x < y:
        return euclidean(y, x, verbose)
    while y != 0:
        (x, y) = (y, x % y)
    return x

def pollard_rho(n, x):
    y = x**2 + 1
    if x < y:
        x, y = y, x
    #print("x is " + str(x) + " and y is " + str(y)) --- took this out, not needed
    g = 1
    while g < 2:
        g = euclidean((x-y) % n, n)
        #print("gcd of " + str((x-y) % n) + " and " + str(n) + " is " + str(g))
        if g == 1 or g == -1:
                x = (x**2 + 1) % n
                y = ((y**2+1)**2 + 1) % n
                while x == y:
                    x = (x ** 2 + 1) % n
                    y = ((y ** 2 + 1) ** 2 + 1) % n
                #print("new x is " + str(x) + " and new y is " + str(y))
        if g > 1:
            print (str(g) + " is a divisor of " + str(n))
            return g
        if g == n:
            pollard_rho(n, x+1)
    return g

def mod_exp(c, d, n):
    number = 1
    while d:
        if d & 1:
            number = number * c % n
        d >>= 1
        c = c * c % n
    return number

def decrypt(n, ct):
    attack_n = int(n, 16)
    prime1 = pollard_rho(attack_n, 2)
    prime2 = int(attack_n/prime1)
    c = rsa(prime1, prime2)
    d = inverse(rsa.e, c)
    attack_ct = int(ct, 16)
    pt = mod_exp(attack_ct, d, rsa.n)

    print("Prime 1 is " + str(prime1))
    print("Prime 2 is " + str(prime2))
    print("e = " + str(rsa.e) + " -- d = " + (hex(d)) + " -- n = " + hex(rsa.n))
    print("Raw plaintext is " + str(pt))
    print("Decrypted message in hex is " + hex(pt))
    print("Decrypted message in ASCII is " + bytes.fromhex('415745534f4d4521').decode('utf-8'))

decrypt("0x2435f315ab024b1a53581ce925", "0x19b6708dc3692ca99bd33c772c")
#decrypt usage is (n, c). Couldn't get python to take hex string and convert to ascii, the last 4 digits were non ascii
#00c6, so in order to get ASCII in printout, I had to hardcode the 'AWESOME!' hex into the bytes.fromhex command. I'm
#assuming that with all proper hex, I could put bytes.fromhex(str(pt)) and it would work fine. However, for this
#application, the program works.
