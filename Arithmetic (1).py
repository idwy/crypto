def egcd(a, b): #Théorème d'Euclide étendu
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return u, v, a

def gcd(a, b): #Théorème d'Euclide
    a, b = (b, a) if a < b else (a, b)
    while b:
        a, b = b, a % b
    return a

def modInverse(e, n): #Théorème de Modulo Inverse
    return egcd(e, n)[0] % n

def totient(p, q): #phi(n)
    return (p - 1) * (q - 1)

def bitlength(x):
    assert x >= 0
    n = 0
    while x > 0:
        n = n + 1
        x = x >> 1
    return n

def isqrt(n):
    if n < 0:
        raise ValueError('Nombre négatif')

    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y

def is_perfect_square(n):
    h = n & 0xF

    if h > 9:
        return -1

    if h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8:
        t = isqrt(n)
        if t * t == n:
            return t
        else:
            return -1

    return -1

def premier(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True