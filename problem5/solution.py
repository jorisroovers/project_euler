# 2520 is the smallest number that can be divided by each of the numbers from 
# 1 to 10 without any remainder. What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20?
# Solution: 232792560

import sys

def print_usage():
    print "usage: python %s <range-end>" % sys.argv[0]

def assert_correct_input():
    if len(sys.argv) != 2:
        print_usage()
        quit(1)

def range_dividers(range_end):
    result = []
    for i in xrange(range_end, 2, -1):
        all_good = True
        for j in result:
            if j % i == 0:
                all_good = False
        if all_good:
            result.append(i) 
    return result

def divisible_by_range(num, r):
    for i in r:
        if not num % i == 0:
            return False

    return True

if __name__ == "__main__":
    assert_correct_input()

    end = int(sys.argv[1])
    num = 1
    r = range_dividers(end)
    while True:
        if divisible_by_range(num, r):
            break
        num += 1       
   
    print "Solution:", num 

