
def sum_range_n(n):
    """ Returns the sum of the first n numbers"""
    # Well-known formula
    return (n*(n+1))/2

if __name__ == "__main__":

    n = 100
    sum_squares = 0
    for i in xrange(1, n +1):
        sum_squares += i**2

    print "Sum Squares =", sum_squares
    squared_sum = sum_range_n(n) ** 2
    print "Squared Sum = ", squared_sum
    print "Solution =", (squared_sum - sum_squares)        
