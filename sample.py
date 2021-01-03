import hashlib
import os

# TODO Fix Bug

sampleString = 'Hello World'

sampleNumber = 126 * 256


def check_prime_and_good_check(prime, g):
    good_prime_bits_count = 2048
    if prime < 0 or prime.bit_length() != good_prime_bits_count:
        raise ValueError('bad prime count {}, expected {}'.format(
            prime.bit_length(), good_prime_bits_count))

    # TODO This is awfully slow
    if factorization.Factorization.factorize(prime)[0] != 1:
        raise ValueError('given "prime" is not prime')

    if g == 2:
        if prime % 8 != 7:
            raise ValueError('bad g {}, mod8 {}'.format(g, prime % 8))
    elif g == 3:
        if prime % 3 != 2:
            raise ValueError('bad g {}, mod3 {}'.format(g, prime % 3))
    elif g == 4:
        pass
    elif g == 5:
        if prime % 5 not in (1, 4):
            raise ValueError('bad g {}, mod5 {}'.format(g, prime % 5))
    elif g == 6:
        if prime % 24 not in (19, 23):
            raise ValueError('bad g {}, mod24 {}'.format(g, prime % 24))
    elif g == 7:
        if prime % 7 not in (3, 5, 6):
            raise ValueError('bad g {}, mod7 {}'.format(g, prime % 7))
    else:
        raise ValueError('bad g {}'.format(g))

    prime_sub1_div2 = (prime - 1) // 2
    if factorization.Factorization.factorize(prime_sub1_div2)[0] != 1:
        raise ValueError('(prime - 1) // 2 is not prime')