from other_functions import factorsproduct, notfactors_forprime


# Some functions are implemented below to obtain or verify prime numbers.
# Some of them are similar to functions from SymPy library.

# Note: The functions are not very efficient for big numbers.
#       For example, the function allprevprimes(n) is not efficient for n > 10**6.
#       For big numbers, it is recommended to use the functions from SymPy library or
#       use the primality_test function from primality_test.py file.


def inefficient_isprime(n: int) -> bool:
    # Inefficient (and simpliest) way to verify if a number is prime or not.
    """
    Args :
        n: int - n >= 1
    Returns :
        bool - True if n is prime, False otherwise.
    """
    for k in range(2, n):
        if n % k == 0:
            return False
    return True



def isprime(n: int) -> bool:
    # More "efficient" way to verify if a number is prime or not. Not very efficient for big numbers.
    """
    Args :
        n: int - n >= 1
    Returns :
        bool - True if n is prime, False otherwise.
    """
    if (n % 2 == 0 and n > 2)\
            or (n % 3 == 0 and n > 3)\
            or (n % 5 == 0 and n > 5)\
            or n<2:
        return False
    k = 7
    while n**(1/2) >= k:
        if n % k == 0 and n**(1/2) >= k:
            return False
        k += 2
        if n % k == 0 and n**(1/2) >= k:
            return False
        k += 2
        if n % k == 0 and n**(1/2) >= k:
            return False
        k += 2
        if n % k == 0 and n**(1/2) >= k:
            return False
        k += 4
    return True



def allprevprimes(n: int) -> list:
    """
    Args :
        n: int - n >= 2
    Returns :
        list - A list of all primes <= n.
    """
    prime_numbers = [2]
    i = 3
    while n >= i:
        if notfactors_forprime(prime_numbers, i):
            prime_numbers.append(i)
        i += 2
    return prime_numbers



def arecoprime(a: int, b: int) -> bool:
    # It verifies if two numbers doesn't have factors in common.
    # Checkout the definition of CoPrimes for more info.
    """
    Args :
        a: int - a >= 1
        b: int - b >= 1
    Returns :
        bool - True if a and b are coprime, False otherwise.
    """
    if (a % 2 == 0) and (b % 2 == 0):
        return False
    k = 3
    if a > b:
        while a > k:
            if (a % k == 0) and (b % k == 0):
                return False
            k += 2
    else:
        while b > k:
            if (a % k == 0) and (b % k == 0):
                return False
            k += 2
    return True



def nextprime(n: int) -> int:
    """
    Args :
        n: int - n >= 1
    Returns :
        int - The next prime > n.
    """
    prime_numbers = allprevprimes(n)
    if n % 2 == 0:
        n += 1
    while True:
        if notfactors_forprime(prime_numbers, n):
            return n
        n += 2



def prevprime(n: int) -> int:
    """
    Args :
        n: int - n >= 1
    Returns :
        int - The previous prime < n.
    """
    prime_numbers = allprevprimes(n-1)
    return prime_numbers[len(prime_numbers)-1]



def primerange(a: int, b: int) -> list:
    """
    Args :
        a: int - a >= 1
        b: int - b >= 1
    Returns :
        list - A list of prime numbers in the range [a, b[.
    """
    prime_numbers = allprevprimes(a)
    final_list = []
    if a <= 2:
        a = 2
        if b > 2:
            final_list.append(2)
    elif isprime(a):
        final_list.append(a)
    while a < b:
        if notfactors_forprime(prime_numbers, a):
            prime_numbers.append(a)
            final_list.append(a)
        a += 1
    return final_list



def primepi(n: int) -> int:
    """
    Args :
        n: int - n >= 1
    Returns :
        int - The number of prime numbers <= n.
    """
    num = len(allprevprimes(n))
    return num



def sheldonprime(n: int) -> bool:
    # Checkout the definition of sheldon prime for more info.
    """
    Args :
        n: int - n >= 1
    Returns :
        bool - True if n is a sheldon prime, False otherwise.
    """
    inverse_number = int(str(n)[::-1])
    sum_num = int(factorsproduct(list(str(n))))
    inverse_sum = int(str(sum_num)[::-1])
    if not isprime(n) or not isprime(inverse_number):
        return False
    if n > inverse_number:
        prime_numbers = allprevprimes(n)
    else:
        prime_numbers = allprevprimes(inverse_number)
    primepi_n = prime_numbers.index(n) + 1
    primepi_inv = prime_numbers.index(inverse_number) + 1
    if primepi_n != sum_num or inverse_sum != primepi_inv:
        return False
    return True



def prime(nth: int) -> int:
    """
    Args :
        nth: int - nth >= 1
    Returns :
        int - The nth prime number.
        In case nth < 1, returns None.
    """
    prime_numbers = [2]
    i = 3
    num = 1
    if nth < 1:
        return None
    elif nth == 1:
        return 2
    while nth > num:
        if notfactors_forprime(prime_numbers, i):
            prime_numbers.append(i)
            num += 1
        i += 2
    return i-2
