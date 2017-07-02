import random
import GenerateurDesCles, RSAWienerHack, Arithmetic, CRT

def generate_random_keypair():
    return GenerateurDesCles.generateKeys(16)

def generate_keypair(p, q):
    if not (Arithmetic.premier(p) and Arithmetic.premier(q)):
        raise ValueError('Les deux nombres doivent être premiers!')
    elif p == q:
        raise ValueError('p et q ne peuvent pas être égaux!')
    n = p * q
    phi = (p - 1) * (q - 1)

    good_d = False
    while not good_d:
        d = random.getrandbits(4)
        if Arithmetic.gcd(d, phi) == 1 and 3 * pow(d, 4) < n:
            good_d = True

    e = Arithmetic.modInverse(d, phi)
    return e,n,d


def encrypt(e, n, plaintext):

    chaine = ''
    for lettre in plaintext:
        chaine += str(pow(ord(lettre), e, n))
        chaine += ' '
    cipher = chaine[0:-1]
    print(cipher)

    return cipher


def decrypt(d,n, ciphertext):
    listcipher = []
    text = list(ciphertext.split(' '))
    for i in range(0, len(text)):
        listcipher.append(int(text[i]))

    listmsg = [chr(pow(char, d, n)) for char in listcipher]

    return ''.join(listmsg)

def decryptCRT(d, p, q, ciphertext):
    listcipher = []
    text = list(ciphertext.split(' '))
    for i in range(0, len(text)):
        listcipher.append(int(text[i]))

    listmsg = [chr(CRT.CRT_RSA(d, p, q, entier)) for entier in listcipher]

    return ''.join(listmsg)

def attack_wiener(e, n, code):
    d = RSAWienerHack.hack_RSA(e, n)

    listcipher = []
    text = list(code.split(' '))
    for i in range(0, len(text)):
        listcipher.append(int(text[i]))

    listmsg = [chr(pow(char,d,n)) for char in listcipher]
    msg = ''.join(listmsg)
    print(msg)

    return msg,d

def attack_hastad(e, listn, listcode):
    lettre = []
    text = []
    for i in range(0,e):
        text.append(list(listcode[i].get().split(' ')))

    for i in range(0,len(text[0])):
        lettre.append([])
        for j in range(0, e):
            lettre[i].append(int(text[j][i]))

    n = [element.get() for element in listn]
    listmsg = []
    for entier in lettre:
        listmsg.append(chr(CRT.CRTmethod(e, n, entier)))

    return ''.join(listmsg)

