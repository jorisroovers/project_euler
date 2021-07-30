########################################################################################################################
# Problem 26: 1000-digit Fibonacci number
########################################################################################################################

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
# 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

########################################################################################################################
# NOTES
# - I'm taking a string based approach, actually looking for the repeating string. I know there's mathematical solutions
#   to this problem, but they eluded me when looking at this problem.
# - Since we're only looking for the length of the 'repetend' (= official term, see wikipedia), it doesn't matter
#   whether we detect the 'correct' repetend, the length of the repetition will be the same
#   e.g. 1234/1234/1234 = repeating part is 4, is same as 4123/4123/4123, length still 4
########################################################################################################################


from common.util import LOG

from decimal import Decimal, getcontext

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

def run(args):

    # We need to use Decimal package to get high precision
    precision = 3000
    getcontext().prec = precision

    overall_longest_repetend = ""
    d_overall_longest_repetend = -1

    for d in range(2, 1000):
        d_fraction = Decimal(1) / Decimal(d)
        d_str = str(d_fraction)

        # Strip off first 10 digits, we *assume*  the repetition will have started at that point
        # Also strip off last digit since that will be rounded
        fraction_part = d_str[10:-1]
        
        # Only consider infinite fractions
        if (len(fraction_part) < (precision-9)):
            continue
        
        # Progressively consider longer repetends
        curr_length = 0
        longest_repetend = "*"
        while curr_length <= len(fraction_part)/2:
            candidate_repetend = fraction_part[0:curr_length+1]
            repeated_str = repeat_to_length(candidate_repetend, len(fraction_part))

            # A candidate repetend is an actual one if it repeats in the for the length of the entire string
            # and does not repeat the previous longest repetend (= same as ends with it)
            if (fraction_part == repeated_str) and not (candidate_repetend.endswith(longest_repetend)):
                longest_repetend = candidate_repetend

            curr_length += 1

        LOG.debug(f"1/{d}={d_str} {longest_repetend} (LEN={len(longest_repetend)})")

        if len(overall_longest_repetend) < len(longest_repetend):
            overall_longest_repetend = longest_repetend
            d_overall_longest_repetend = d
        
    print(f"SOLUTION: {d_overall_longest_repetend} (repend: {overall_longest_repetend}, LEN={len(overall_longest_repetend)})")
