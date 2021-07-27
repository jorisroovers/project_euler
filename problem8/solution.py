# The four adjacent digits in the 1000-digit number that have the greatest 
# product are 9 x 9 x 8 x 9 = 5832. Find the thirteen adjacent digits in the 
# 1000-digit number (see input.txt) that have the greatest product. 
# What is the value of this product?
import sys
import os

from functools import reduce

def run(args):
    # input.txt sits next to solution.py, get absolute path
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file, 'r') as f:
        contents = f.readlines()
        # input file as single str
        number_str = "".join(contents).replace("\n", "")
        print("Number")
        print(number_str)
        print("-"*50)
        i = 0
        window_size = int(args[1])
        last_window_start_index = len(number_str) - window_size
        largest_product = 0
        largest_window = ""
        while i <= last_window_start_index:
            window = number_str[i:i+window_size]
            #print "window: %s", window
            product = reduce(lambda x, y: int(x) * int(y), window)
            if product > largest_product:
                largest_product = product
                largest_window = window
            i += 1

        window_product_str = "x".join([ch for ch in largest_window])
        print("Solution: %i (%s)" % (largest_product, window_product_str))


if __name__ == "__main__":
    run(sys.argv)

