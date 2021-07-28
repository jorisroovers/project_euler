########################################################################################################################
# Problem 17: Lexicographic permutations
########################################################################################################################

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage
########################################################################################################################
# NOTES
# 
#
########################################################################################################################

from common.util import LOG

below_twenty = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ignore", "ignore", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def get_string_repr(i):
    i_str = str(i)
    if i < 20:
        str_repr = below_twenty[i]
    elif len(i_str) == 2:
        str_repr = tens[int(i_str[0])] + below_twenty[int(i_str[1])]
    elif len(i_str) == 3:
        str_repr = below_twenty[int(i_str[0])] + "hundred"
        if i % 100 > 0:
            str_repr += "and" + get_string_repr(int(i_str[1:]))
    elif i == 1000:
        str_repr = "onethousand"
    return str_repr

def run(args):
    letter_count = 0
    for i in range(1, 1001):
        str_repr = get_string_repr(i)
        LOG.debug(f"{i} {str_repr} {len(str_repr)}")
        letter_count += len(str_repr)

    print("SOLUTION:", letter_count)

