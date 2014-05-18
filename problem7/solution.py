# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# Solution: 104743
import sys

def print_usage():
    print "usage: python %s <number>" % sys.argv[0]

def assert_correct_input():
    if len(sys.argv) != 2:
        print_usage()
        quit(1)

def is_prime(number):
    """ Checks whether a number is a prime number """
    if number == 1 or number == 2:
        return True
    for i in xrange(2, number/2 + 1):
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

if  __name__ == "__main__":
    assert_correct_input()
    target = int(sys.argv[1]) + 1 # we don't count 1 as a prime in this problem

    num = 1
    one_percent = target / 100
    for prime in generate_primes():
        if num == target:
            solution = prime
            break

        # Let's print some percentages while we wait
        if num % one_percent == 0:
            percentage = float(num) / float(target) * 100.0
            print "%d%%" % percentage
        num += 1

    print "Solution:", solution



 
    
 
