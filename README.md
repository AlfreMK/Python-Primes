# Prime Functions for Python

Some functions to play with prime numbers __for python__.

Some of them are similar (or equal) to functions from SymPy library.

Implemented functions:
- `inefficient_isprime(n)`: Inefficient (and simpliest) way to verify if a number is prime or not. Returns True if integer n is prime.
- `isprime(n)`: More efficient way to verify if a number is prime or not. Returns True if integer n is prime.
- `allprevprime(n)`: Efficient way of making a list of primes <= n.
- `arecoprime(a,b)`: It verifies if two numbers doesn't have factors in common. Checkout the definition of CoPrimes for more info. Returns True if a and b are coprimes.
- `nextprime(n)`: Returns the next prime > n.
- `prevprime(n)`: Returns the previous prime < n.
- `primerange(a, b)`: Returns a list of prime numbers in the range [a, b[.
- `primepi(n)`: Returns the number of prime numbers <= n.
- `sheldonprime(n)`: Returns True if number n is a sheldon prime. Checkout the definition of sheldon prime to more info.
- `prime(nth)`: Returns nth prime number. In case nth < 1, returns None.

Also is featured the primality test (in this case, Solovay-Strassen primality test). It is a randomised probabilistic test, so it can verify if a number is prime. it is very efficient and it is implemented in the `primality_test` file.

Other functions:
- `notfactors(list)`: Returns True if no number in list is factor of n.
- `factorsproduct(list)`: Returns the product of all elements of a list in a recursive way. Returns a float.
- `notfactors_forprime(list)`: Variation of notfactors function for more efficiency. Useful to determine if n is prime if the numbers of `list` are sorted and are primes < n.