import logging

logging.basicConfig()
LOG = logging.getLogger('euler')

########################################################################################################################
# Utility functions

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

def is_palindrome(num):
    """ Checks whether a given number is a palindrome"""
    # iterate over first half of the string, find corresponding
    # letter in second half of the string and check if they are the same.
    num_str = str(num)
    num_str_len = len(num_str)
    for left_i in range(0, int(num_str_len/2)):
        right_i = (num_str_len - 1) - left_i
        # print left_i, "==", right_i
        if num_str[left_i] != num_str[right_i]:
            return False
    return True


def divisors(num):
    """ Return a sorted list of divisors for a given number """
    cur = 1
    end = num
    # we use a set to avoid situations where we add the middle 2 divisors twice
    result = set()
    while cur <= end:
        mod = num % cur
        end = num // cur
        if mod == 0:
            result.add(cur)
            result.add(end)
        cur += 1

    return sorted(result)

def proper_divisors(num):
    """ Return a sorted list of proper divisors
    A proper divisor of a number is any divisor of that number other than the number itself """
    result = divisors(num) # using `pop()` is more efficient (O(1)) that using slicing `[:-1]` (O(n))
    if len(result) > 0:
        result.pop()
    return result
