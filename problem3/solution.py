########################################################################################################################
# Problem 3: Largest prime factor
########################################################################################################################
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
########################################################################################################################
# NOTES
# - Need to revisit this problem, the current solution is just a brute-force that takes a long time to complete.
########################################################################################################################

def print_usage(args):
    print("usage: python %s <number>" % args[0])

def assert_correct_input(args):
    if len(args) != 2:
        print_usage()
        quit(1)

def is_prime(number):
    """ Checks whether a number is a prime number """
    if number == 1 or number == 2:
        return True
    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            return False
    return True

def generate_primes():
    """ 
    Generator for prime numbers.
    Not used as current solution is more performant.
    """
    i = 1
    while True:
        if is_prime(i):
            yield i
        i += 1


def is_factor(factor, number):
    return number % factor == 0

def run(args):
    assert_correct_input(args)
    number = int(args[1])
    largest_prime_factor = 0

    factor = 0
    for prime in generate_primes():
        print(prime, factor)
        if is_factor(prime, number):
            largest_prime_factor = prime
            print("prime factor=", prime, factor)
        factor = number / prime
        if prime >= factor:
            break

    print("Solution:", largest_prime_factor)

