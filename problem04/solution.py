########################################################################################################################
# Problem 4: Largest palindrome product
########################################################################################################################
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
########################################################################################################################
# NOTES
#
########################################################################################################################

from common.util import is_palindrome

def run(args):
        
    three_digit_numbers = range(100, 1000)

    max_palindrome = 0
    for i in three_digit_numbers:
        for j in three_digit_numbers:
            product = i*j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    
    print("Solution: ", max_palindrome)
     
