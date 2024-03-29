########################################################################################################################
# Problem 20: Factorial digit sum
########################################################################################################################

# n! means n x (n - 1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3+6+2+8+8+0+0=27.
# Find the sum of the digits in the number 100!

########################################################################################################################
# NOTES
# 
########################################################################################################################

def run(args):

    n = int(args[1])
    print("N=%d" % n)

    factorial = 1

    for i in range(1, n+1):
        factorial = factorial * i
        print("%d!=%d" % (i, factorial))
        
    print("factorial(%d)=%d" % (n, factorial))

    sum = 0
    for ch in str(factorial):
        sum += int(ch)
        
    print("digit sum of '%d'= %d" % (factorial, sum))
