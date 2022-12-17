import random


# The following code is extracted from the following link:
# https://github.com/IIC2283/DAA-2022-2/blob/main/codigo/alg_teoria_numeros.py
# all credits to the authors of the code.

# This is a python implementation of the Solovay-Strassen primality test.
# A randomised algorithm to test if a number is prime or not.

def isprime(n: int, k: int = 100) -> bool:
    """
    Args :
        n: int - n >= 1
        k: int - k >= 1
    Returns :
        bool - True if n is a prime number, and False in other case.
        The probability of error of the test is less or equal to 2**(-k),
        and it is based on the Solovay-Strassen primality test.
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    elif is_power(n):
        return False
    neg = 0
    for i in range(1,k+1):
        a = random.randint(2,n-1)
        if gcd(a,n) > 1:
            return False
        else:
            b = exp_mod(a,(n-1)//2,n)
            if b == n - 1:
                neg = neg + 1
            elif b != 1:
                return False
    if neg > 0:
        return True
    else:
        return False



def is_power(n: int) -> bool:
    """
    Args :
        n: int - n >= 1
    Returns :
        bool - True if there is a natural number a and a natural number b such that n = (a**b),
        where a >= 2 and b >= 2. In other case returns False.
    """
    if n <= 3:
        return False
    else:
        k = 2
        lim = 4
        while lim <= n:
            if has_int_root(n, k):
                return True
            k = k + 1
            lim = lim * 2
        return False



def exp_mod(a: int, b: int, n: int) -> int:
    """
    Args :
        a: int
        b: int
        n: int - n > 0
    Returns :
        int - a**b in module n
    """
    if b == 0:
        return 1
    elif b > 0:
        res = 1
        pot = a
        while b > 0:
            if b % 2 == 1:
                res = (pot * res) % n
            b = b // 2
            pot = (pot * pot) % n
        return res
    else:
        return exp_mod(modular_inverse(a,n),-b,n)

    

def gcd(a: int, b: int) -> int:
    """
    Args :
        a: int
        b: int - a > 0 o b > 0
    Returns :
        greatest common divisor between a & b
    """
    while b > 0:
        temp = b
        b = a % b
        a = temp
    return a



def has_int_root(n: int, k: int) -> bool:
    """
    Args :
        n: int - n >= 1
        k: int - k >= 2
    Returns :
        bool - True if there is a natural number a such that n = (a**k),
        where a >= 2. In other case returns False.     
    """
    if n <= 3:
        return False
    else:
        a = 1
        while exp(a,k) < n:
            a = 2*a
        return has_int_root_interval(n, k, a//2, a)


    
def has_int_root_interval(n: int, k: int, i: int, j: int) -> bool:
    """
    Args :
        n: int - n >= 1
        k: int - k >= 2
        i: int - i >= 0
        j: int - j >= 0
    Returns :
        bool - True if there is a natural number a such that n = (a**k),
        where i <= a <= j. In other case returns False.
    """
    while i <= j:
        if i==j:
            return n == exp(i,k)
        else:
            p = (i + j)//2 
            val = exp(p,k)
            if n == val:
                return True
            elif val < n:
                i = p+1
            else:
                j = p-1
    return False


def exp(a: int, b: int) -> int:
    """
    Args :
        a: int
        b: int - b >= 0
    Returns :
        int - a**b
    """
    if b == 0:
        return 1
    else:
        res = 1
        pot = a
        while b > 0:
            if b % 2 == 1:
                res = pot * res
            b = b // 2
            pot = pot * pot
        return res



def modular_inverse(a: int, n: int) -> int:
    """
    Args :
        a: int - a >= 1
        n: int - n >= 2, a & n coprimes
    Returns :
        int - inverse of a in module n
    """
    (r, s, t) = alg_ext_euclides(a, n)
    return s % n



def alg_ext_euclides(a: int, b: int) -> tuple:
    """
    Args :
        a: int
        b: int - a >= b >= 0 y a > 0
    Returns :
        (int , int , int) - greatest common divisor GCD(a, b) between a and b,
        and integers s and t such that GCD(a, b) = s*a + t*b
    """
    r_0 = a
    s_0 = 1
    t_0 = 0
    r_1 = b
    s_1 = 0
    t_1 = 1
    while r_1 > 0:
        r_2 = r_0 % r_1
        s_2 = s_0 - (r_0 // r_1) * s_1
        t_2 = t_0 - (r_0 // r_1) * t_1
        r_0 = r_1
        s_0 = s_1
        t_0 = t_1
        r_1 = r_2
        s_1 = s_2
        t_1 = t_2
    return r_0, s_0, t_0
