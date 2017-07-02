import Arithmetic

def crt_pow(entier, d, pq):
    entier %= pq
    d %= pq-1
    return pow(entier, d, pq)


def CRT_RSA(d, p, q, entier):
    n = p * q
    _p = n / p
    _q = n / q

    x1 = crt_pow(entier,d,p)
    x2 = crt_pow(entier,d,q)

    part1 = x1 * _p * Arithmetic.modInverse(_p, p)
    part2 = x2 * _q * Arithmetic.modInverse(_q, q)

    return int((part1+part2) % n)


def CRTmethod(e, n, entier):
    N = 1
    for element in n:
        N *= element

    _n = [int((N / element)) for element in n]
    modinv = [Arithmetic.modInverse(_n[i], n[i]) for i in range(0,e)]
    result = [(entier[i] * _n[i] * modinv[i]) for i in range(0,e)]

    summod = sum(result) % N
    msg = round(pow(summod, 1/e))

    return msg

















