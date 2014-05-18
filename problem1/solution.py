# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import sys

def print_usage():
    print "usage: python %s <range-end>" % sys.argv[0]

def assert_correct_input():
    if len(sys.argv) != 2:
        print_usage()
        quit(1)

if __name__ == "__main__":
    assert_correct_input()
    
    end = int(sys.argv[1])
    numbers = range(1, end)
    terms = []

    for number in numbers:
        if (number % 3 == 0) or (number % 5 == 0):
            terms.append(number)

    print "Terms:"
    print terms  
    solution = reduce(lambda x, y: x+y, terms)      
    print "Solution:", solution

