########################################################################################################################
# Problem 25: 1000-digit Fibonacci number
########################################################################################################################

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

########################################################################################################################
# NOTES
# 
########################################################################################################################

from common.util import xfib, LOG

def run(args):

    i = 1
    for fi in xfib():
        fi_str_len = len(str(fi))
        LOG.debug(f"F_{i}={fi} ({fi_str_len})")
        if fi_str_len == 1000:
             print(f"SOLUTION: {i}")
             break
        i += 1