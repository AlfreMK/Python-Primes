import time
import sympy
import prime_functions



def time_comparison(function1, function2, n):
    two_parameters = False
    print("###################################")
    print("Attended functions:\n", str(function1), "\n", str(function2))
    print("Running...\n")
    if type(n) == list or type(n) == tuple:
        two_parameters = True
        start_time = time.time()
        result1 = function1(*n)
        time1 = time.time() - start_time
        start_time = time.time()
        result2 = list(function2(*n))
        time2 = time.time() - start_time
        output_bool = result1 == result2
    else:
        start_time = time.time()
        result1 = function1(n)
        time1 = time.time() - start_time
        start_time = time.time()
        result2 = function2(n)
        time2 = time.time() - start_time
        output_bool = result1 == result2
    print("### PrimeFunctionsPy performance ###")
    print("Output:", result1)
    print("--- %s seconds ---" % (time1))
    print("######## SymPy performance ########")
    print("Output:", result2)
    print("--- %s seconds ---" % (time2))
    print("Same output?", output_bool)
    if not output_bool and two_parameters:
        diff_list = []
        for k in range(max(len(result1), len(result2))):
            k = result1[k]
            if (k not in result1 and k in result2) or (k in result1 and k not in result2):
                diff_list.append(k)
        print("Diff list:", diff_list)
    print("###################################")
    

def main():
    # prime(n) time comparison
    time_comparison(prime_functions.prime, sympy.prime, 10000)

    # primerange(a, b) time comparison
    time_comparison(prime_functions.primerange, sympy.primerange, (3, 50))



if __name__ == '__main__':
    main()
