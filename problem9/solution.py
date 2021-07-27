########################################################################################################################
# Problem 9: Special Pythagorean triplet
# ########################################################################################################################
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
########################################################################################################################
# NOTES
#
########################################################################################################################

# Very inefficient, but does the job
def run(args):

    total = 1000
    def find_abc():
        for a in range(1, total+1):
            for b in range(1, total+1):
                if a + b > total:
                    continue
                for c in range(1, total+1):
                    if a + b + c == total:
                        if (a**2 + b**2) == c**2:
                            return (a, b, c)
    a, b, c = find_abc()
    print("Solution: ", (a*b*c))
    
