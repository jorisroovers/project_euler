def is_prime(number):
    """ Checks whether a number is a prime number """
    if number == 1 or number == 2:
        return True
    if number == 0:
        return False

    end = number/2 + 1
    i = 2
    while i < end:
        if number % i == 0:
            return False
        end = number / i
        i += 1

    return True

def generate_primes():
    """
    Generator for prime numbers.
    """
    i = 1
    while True:
        if is_prime(i):
            yield i
        i += 1

def xfib():
    """ Infinite generator for Fibonacci numbers"""
    f1 = 1
    f2 = 1
    while True:
        yield f1
        tmp = f2
        f2 = f1 + f2
        f1 = tmp
