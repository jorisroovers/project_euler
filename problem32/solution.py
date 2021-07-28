
########################################################################################################################
# Problem 32: Pandigital products
########################################################################################################################

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, 
# the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
# 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
# pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

########################################################################################################################
# NOTES
# - The key here is to realize that creating all possible multiplications is the same as creating all permutations of
#   the list ("1", "2", "3", "4", "5", "6", "7", "8", "9", "x", "=") and then filtering out invalid identities.
# 
########################################################################################################################

from itertools import permutations
from common.util import LOG

def run(args):
    digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    operators = ('x', '=')
    unique_products = set()
    for identity in permutations(digits+operators):
        identity = "".join(identity)
        # 1. Filter out invalid identities:
        # A. Those that start or end with operators
        if identity[0] in operators or identity[-1] in operators:
            continue
        # B. Those that have x and = next to eachother
        if "x=" in identity or "=x" in identity:
            continue

        # C. Those that have = before x (these identities are covered in a later permutation)
        if identity.index("=") < identity.index("x"):
            continue

        # 2. Parse identity into its parts
        parts = {}
        part_name = "multiplicand"
        for c in identity:
            if c == "x":
                part_name = "multiplier"
                continue
            elif c == "=":
                part_name = "product"
                continue
            parts[part_name] = parts.get(part_name, "") + c

        # 3. Evaluate identity and see if it's correct
        if int(parts['multiplicand']) * int(parts['multiplier']) == int(parts['product']):
            LOG.debug(f"{identity} {parts}")
            unique_products.add(int(parts['product']))


    LOG.debug(f"Unique products {unique_products}")
    print("SOLUTION", sum(unique_products))
