########################################################################################################################
# Problem 7: 10001st prime
########################################################################################################################
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
########################################################################################################################
# NOTES
#
########################################################################################################################

from common.util import generate_primes

def print_usage():
    print("arguments:  <number>")

def assert_correct_input(args):
    if len(args) != 2:
        print_usage()
        quit(1)

def run(args):
    assert_correct_input(args)
    target = int(args[1]) + 1 # we don't count 1 as a prime in this problem

    num = 1
    one_percent = target / 100
    for prime in generate_primes():
        if num == target:
            solution = prime
            break

        # Let's print some percentages while we wait
        if num % one_percent == 0:
            percentage = float(num) / float(target) * 100.0
            print("%d%%" % percentage)
        num += 1

    print("Solution:", solution)

 
