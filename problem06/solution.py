########################################################################################################################
# Problem 6: Sum square difference
########################################################################################################################
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 +2 + .... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
########################################################################################################################
# NOTES
#
########################################################################################################################

def sum_range_n(n):
    """ Returns the sum of the first n numbers"""
    # Well-known formula
    return (n*(n+1))/2

def run(args):

    n = 100
    sum_squares = 0
    for i in range(1, n +1):
        sum_squares += i**2

    print("Sum Squares =", sum_squares)
    squared_sum = sum_range_n(n) ** 2
    print("Squared Sum = ", squared_sum)
    print("Solution =", int((squared_sum - sum_squares)))
