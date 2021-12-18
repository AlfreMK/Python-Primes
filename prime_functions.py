from other_functions import factorsproduct, notfactors_forprime


# Some functions are implemented below to obtain or verify prime numbers.
# Some of them are similar to functions from SymPy library.


def inefficient_isprime(n) -> bool:
# Inefficient (and simpliest) way to verify if a number is prime or not.
    for k in range(2, n):
        if n % k == 0:
            return False
    return True


def isprime(n) -> bool:
# More efficient way to verify if a number is prime or not.
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


def allprevprimes(n) -> list:
# Efficient way of making a list of primes <= n
    prime_numbers = [2]
    i = 3
    while n >= i:
        if notfactors_forprime(prime_numbers, i):
            prime_numbers.append(i)
        i += 2
    return prime_numbers


def arecoprime(a,b) -> bool:
# It verifies if two numbers doesn't have factors in common.
# Checkout the definition of CoPrimes for more info.
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


def nextprime(n) -> int:
# Returns the next prime > n.
    prime_numbers = allprevprimes(n)
    if n % 2 == 0:
        n += 1
    while True:
        if notfactors_forprime(prime_numbers, n):
            return n
        n += 2


def prevprime(n) -> int:
# Returns the previous prime < n.
    prime_numbers = allprevprimes(n-1)
    return prime_numbers[len(prime_numbers)-1]


def primerange(a, b) -> list:
# Returns a list of prime numbers in the range [a, b[.
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


def primepi(n) -> int:
# Returns the number of prime numbers <= n.
    num = len(allprevprimes(n))
    return num


def sheldonprime(n) -> bool:
# Returns True if number n is a sheldon prime.
# Checkout the definition of sheldon prime to more info.
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


def prime(nth) -> int:
# Returns nth prime number.
# In case nth < 1, returns None.
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
