import random, MillerRabin, Arithmetic

def getPrimePair(bits=512):

    assert bits % 4 == 0

    p = MillerRabin.gen_prime(bits)
    q = MillerRabin.gen_prime_range(p + 1, 2 * p)

    return p, q


def generateKeys(nbits):

    assert nbits % 4 == 0

    p, q = getPrimePair(nbits // 2)
    print("p=", p)
    print("q=", q)
    n = p * q
    phi = Arithmetic.totient(p, q)

    good_d = False
    while not good_d:
        d = random.getrandbits(nbits // 4)
        if (Arithmetic.gcd(d, phi) == 1 and 3 * pow(d, 4) < n):
            good_d = True

    e = Arithmetic.modInverse(d, phi)
    return e, n, d
