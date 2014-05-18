# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import sys

def print_usage():
    print "usage: python %s <range-end>" % sys.argv[0]

def assert_correct_input():
    if len(sys.argv) != 2:
        print_usage()
        quit(1)

def is_palindrome(num):
    """ Checks whether a given number is a palindrome"""
    # iterate over first half of the string, find corresponding
    # letter in second half of the string and check if they are the same.
    num_str = str(num)
    num_str_len = len(num_str)
    for left_i in xrange(0, num_str_len/2):
        right_i = (num_str_len - 1) - left_i
        # print left_i, "==", right_i
        if num_str[left_i] != num_str[right_i]:
            return False
    return True


if __name__ == "__main__":
        
    three_digit_numbers = range(100, 1000)
    #print "Three digit numbers"
    #print three_digit_numbers

    max_palindrome = 0
    for i in three_digit_numbers:
        for j in three_digit_numbers:
            product = i*j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    
    print "Solution: ", max_palindrome
     
