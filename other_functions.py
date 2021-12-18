
def notfactors(list1, n) -> bool:
# Returns true if no number in list is factor of n.
    list1 = sorted(list1)
    for i in list1:
        if n % i == 0 and n > i:
            return False
        if n <= i:
            return True
    return True


def notfactors_forprime(list1, n) -> bool:
# Variation of notfactors function for more efficiency
# Useful to determine if n is prime if the numbers of list1 are primes and < n.
    # list = sorted(list)       # necessary only when list is not sorted
    for i in list1[:int((len(list1)+1)**(1/2))+1]:
        if n % i == 0:
            return False
    return True


def factorsproduct(list1) -> float:
# Returns the product of all elements of a list in a recursive way
    if len(list1) == 1:
        return float(list1[0])
    return float(list1[len(list1)-1])*factorsproduct(list1[:len(list1)-1])
