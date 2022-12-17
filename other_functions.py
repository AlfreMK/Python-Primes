

def notfactors(list1: list, n: int) -> bool:
    """
    Args :
        list1: list - list of int
        n: int - n >= 1
    Returns :
        bool - True if no number in list1 is factor of n. In other case returns False.
    """
    list1 = sorted(list1)
    for i in list1:
        if n % i == 0 and n > i:
            return False
        if n <= i:
            return True
    return True



def notfactors_forprime(list1: list, n: int) -> bool:
    # Variation of notfactors function for more efficiency
    # Useful to determine if n is prime if the numbers of list1 are primes and < n.
    """
    Args :
        list1: list - list of int
        n: int - n >= 1
    Returns :
        bool - True if no number in list1 is factor of n. In other case returns False.
    """
    # list = sorted(list)       # necessary only when list is not sorted
    for i in list1[:int((len(list1)+1)**(1/2))+1]:
        if n % i == 0:
            return False
    return True



def factorsproduct(list1: list) -> float:
    # Returns the product of all elements of a list in a recursive way
    """
    Args :
        list1: list - list of int
    Returns :
        float - product of all elements of list1
    """
    if len(list1) == 1:
        return float(list1[0])
    return float(list1[len(list1)-1])*factorsproduct(list1[:len(list1)-1])
