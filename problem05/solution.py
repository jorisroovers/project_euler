########################################################################################################################
# Problem 5: Smallest multiple
########################################################################################################################
# 2520 is the smallest number that can be divided by each of the numbers from 
# 1 to 10 without any remainder. What is the smallest positive number that is 
# evenly divisible by all of the numbers from 1 to 20?
########################################################################################################################
# NOTES
#
########################################################################################################################

# Returns the dividers in a range [1...range_end] that are not dividers
# of a different number within that same range.
# For example:
# [6, 5, 4] is return for input 6, because [1,2,3] are already covered.
# 1 -> everything is divisable by 1, 
# 2 -> 4 and 6 are divisble by 2
# 3 -> 6 is divisble by 3
def range_dividers(range_end):
    result = []
    for i in range(range_end, 2, -1):
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
    
def find_solution(n):
    num = n
    r = range_dividers(n)
    print(r)
    while True:
        if divisible_by_range(num, r):
            break
        num += n
        
    return num

def run(args):
    n = int(args[1])
    for i in range(1, n+1):
        solution = find_solution(i)
        print("N=%d: %d" % (i, solution))
   
    print("Solution:", solution)

