# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys

def print_usage(args):
    print "usage: python solution.py <range-end>"

def assert_correct_input(args):
    if len(args) != 2:
        print_usage(args)
        quit(1)


def run(args):
    assert_correct_input(args)

    end = int(args[1])
    numbers = range(1, end)
    terms = []

    for number in numbers:
        if (number % 3 == 0) or (number % 5 == 0):
            terms.append(number)

    print "Terms:"
    print terms
    solution = reduce(lambda x, y: x+y, terms)
    print "Solution:", solution

if __name__ == "__main__":
    run(sys.argv)
