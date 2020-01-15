# Base code source: https://dev.to/nestedsoftware/big-o-prime-factors-and-pseudo-polynomial-time-55cp
import time
import random

def prime_factors(n):
    results = []

    factor = 2
    while factor * factor <= n:
        (n, intermediate_results) = check_factor(n, factor)
        results += intermediate_results
        factor += 1

    if (n > 1):
        results += [n]

    return results

def check_factor(n, factor):
    results = []

    (q, r) = divmod(n, factor)
    while r == 0:
        results.append(factor)
        n = q
        (q, r) = divmod(n, factor)

    return n, results

def factorize_test(b):
    # Generate 10000 numbers in range
    numbers = []
    for x in range(0, 10000):
        numbers.append(random.randint(2 ** (int(b)-1) + 1, 2 ** int(b)))

    print('== Key size: %s bits ==' % b)
    print('Generated numbers')

    # Start timers and factorize
    print('Starting timer')
    set_start = time.process_time()
    for num in numbers:
        fact = prime_factors(num)
    time_taken = time.process_time() - set_start
    print('Calculations done')
    print('Total time taken: %f seconds' % time_taken)

    # Write results to file for data collection
    line = str(b) + ',' + str(time_taken) + '\n'
    with open('fact_results.csv', 'a') as f:
        f.write(line)

# Time factorization for key sizes 2^8 bits to 2^35 bits
for x in range(3, 35):
    factorize_test(x)