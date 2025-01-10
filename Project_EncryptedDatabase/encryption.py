import random

def gcd(a, b):
    """
    Generate the greatest common divisor between two numbers.

    Parameters:
        a (int): the first integer
        b (int): the second integer

    Returns:
        The greatest common divisor of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """
    Generate the modular inverse of e mod phi using Extended Euclidean Algorithm.
    
    Parameters:
        e (int): the first integer
        phi (int): the second integer
        
    Returns:
        The modular inverse of e % phi.
    """
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
    """
    Check the primality of a number.
    
    Parameters:
        num (int): the number to check
        
    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_number(min_val=100000, max_val=5000000):
    """
    Generate a prime random number.
    
    Parameters:
        min_val (int): the minimum value of the prime number
        max_val (int): the maximum value of the prime number
        
    Returns:
        A prime number within the specified range.
    """
    while True:
        num = random.randint(min_val, max_val)
        if is_prime(num):
            return num

# generate keys -> RSA
def gen_keys():
    """
    Generate public and private keys for RSA encryption.
    
    Returns:
        A tuple containing the public and private keys.
    """
    p = generate_prime_number()
    q = generate_prime_number()
    while q == p: # must be different numbers
        q = generate_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:  #=e must be coprime with phi
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(mes, pub_key):
    """
    Encrypt a message using the public key.
    
    Parameters:
        mes (str): the message to encrypt
        pub_key (tuple): the public key to use
        
    Returns:
        A list of encrypted characters
    """
    e, n = pub_key
    return [pow(ord(char), e, n) for char in mes]

def decrypt(ciph_txt, priv_key):
    """
    Decrypt a message using the private key.
    
    Parameters:
        ciph_txt (list): the list of encrypted characters
        priv_key (tuple): the private key to use
        
    Returns:
        The decrypted message.
    """
    d, n = priv_key
    return ''.join([chr(pow(char, d, n)) for char in ciph_txt])