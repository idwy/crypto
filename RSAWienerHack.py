
import FractionsContinues, Arithmetic

def hack_RSA(e, n):

    frac = FractionsContinues.rational_to_contfrac(e, n)
    convergents = FractionsContinues.convergents_from_contfrac(frac)

    for (k, d) in convergents:

        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1

            discr = s * s - 4 * n
            if discr >= 0:
                t = Arithmetic.is_perfect_square(discr)
                if t != -1 and (s + t) % 2 == 0:
                    print("Hacked!")
                    return d
                else:
                    print("nope")
