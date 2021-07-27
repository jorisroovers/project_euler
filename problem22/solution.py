########################################################################################################################
# Problem 22: Names Scores
########################################################################################################################

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
# 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

########################################################################################################################
# NOTES
# 
########################################################################################################################

import os

def run(args):
    if len(args) == 2:
        input_file = args[1]
    else:
        input_file = os.path.join(os.path.dirname(__file__), "p022_names.txt")

    
    with open(input_file, 'r') as f:
        contents = f.read()
        names = sorted([n.replace('"',"") for n in contents.split(",")])

        total = 0
        for i, name in enumerate(names):
            name_val = 0
            for c in name:
                name_val += (ord(c) - 64) # ASCII 'A'-'Z' = 65-90, just substract 64 to get 1-26 range.
            name_score = (i+1) * name_val
            total += name_score

        print("TOTAL", total)