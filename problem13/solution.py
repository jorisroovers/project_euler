
########################################################################################################################
# Problem 13: Large sum
########################################################################################################################
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# <See input.txt>
########################################################################################################################
# NOTES
#
########################################################################################################################

import os

def run(args):
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_file, 'r') as f:
        contents = f.readlines()
        total = 0
        for number_str in contents:
            print(int(number_str), total)
            total += int(number_str) 

    solution = str(total)[0:10]
    print("Solution:", solution)
