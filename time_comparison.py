import time
import sympy
import prime_functions
import primality_test


def time_comparison(func_list, input):
    results = []
    print('----------------------------------------')
    print(f'Comparing function "{func_list[0].__name__}({input})"')
    print('----------------------------------------')
    for func in func_list:
        start = time.time()
        results.append(func(input))
        end = time.time()
        print(f'{func.__module__} took {end - start} seconds')
    print('----------------------------------------')
    if all(x == results[0] for x in results):
        print(f'All results are equal: {results[0]}')
    else:
        print(f'Not all results are equal: {results}')
    print('----------------------------------------')



def main():
    # isprime(n) time comparison
    time_comparison([prime_functions.isprime, sympy.isprime, primality_test.isprime], 2147483647)

    # for bigger numbers we can't use prime_functions.isprime
    time_comparison([sympy.isprime, primality_test.isprime], 2305843009213693951)



if __name__ == '__main__':
    main()
