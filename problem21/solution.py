########################################################################################################################
# Problem 21: Amicable numbers
########################################################################################################################

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b
# are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

########################################################################################################################
# NOTES
# - This can easily be made more efficient by not considering numbers without divisors (ie. prime numbers) and by not
# recalculating the divisors for sums multiple times by keeping them in a set. But python is fast enough to just
# iterate over all numbers in less than a second, so haven't bothered optimizing this.
#
########################################################################################################################
from common.util import proper_divisors, LOG


def run(_):
    amicable_numbers = set()
    for a in range(10000):
        d_a = sum(proper_divisors(a))
        d_b = sum(proper_divisors(d_a))
        if a != d_a and a == d_b:
            LOG.debug("a=%s b=%s", a, d_a)
            amicable_numbers.add(a)
            amicable_numbers.add(d_a)

    print(sum(amicable_numbers))
