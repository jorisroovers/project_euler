# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Solution: 6857
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

def is_factor(factor, number):
    return number % factor == 0
    #div = float(factor) / float(number)
    #print (div - int(div))

if  __name__ == "__main__":
    assert_correct_input()
    number = int(sys.argv[1])
    largest_prime_factor = 0
    #for i in xrange(number/2 + 1, 1, -1):
    #    print "number ", i
    #    if is_factor(i, number):
    #        print "Checking factor", i
    #        if is_prime(i):
    #            largest_prime_factor = i
    #            break
    

    #print "Solution:", largest_prime_facto
    factor = 0
    for prime in generate_primes():
        print prime, factor
        if is_factor(prime, number):
            largest_prime_factor = prime
            print "prime factor=", prime, factor
        factor = number / prime
        if prime >= factor:
            break            
      
    print "Solution:", largest_prime_factor
 #     if prime > number/2:
   #         break
   #     if is_factor(prime, number):
   #         print prime
 

 
