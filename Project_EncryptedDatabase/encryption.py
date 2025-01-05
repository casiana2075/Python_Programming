import random

def gcd(a, b):
    """generate the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """generate the modular inverse of e mod phi by Extended Euclidean Algorithm"""
    d_old, d_new = 0, 1
    r_old, r_new = phi, e
    while r_new != 0:
        quotient = r_old // r_new
        d_old, d_new = d_new, d_old - quotient * d_new
        r_old, r_new = r_new, r_old - quotient * r_new
    if r_old > 1:
        raise ValueError("e and phi are not coprime.")
    return d_old % phi

def is_prime(num):
    """check the primality of a number"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_number(min_val=100000, max_val=5000000):
    """generate a prime random number"""
    while True:
        num = random.randint(min_val, max_val)
        if is_prime(num):
            return num

# generate keys -> RSA
def gen_keys():
    """RSA"""
    p = generate_prime_number()
    q = generate_prime_number()
    while q == p: # mush have different num
        q = generate_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:  #=e must be coprime with phi
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(mes, pub_key):
    """encript with public keu"""
    e, n = pub_key
    return [pow(ord(char), e, n) for char in mes]

def decrypt(ciph_txt, priv_key):
    """decript with private key"""
    d, n = priv_key
    return ''.join([chr(pow(char, d, n)) for char in ciph_txt])