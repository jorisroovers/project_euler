########################################################################################################################
# Problem 10: Summation of primes
########################################################################################################################
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
########################################################################################################################
# NOTES
# - Not very elegant: Just a for loop around a prime generator and then sum up the results...
########################################################################################################################


from common.util import generate_primes

def assert_usage(args):
    if len(args) != 2:
        print("Required arguments")
        print("\tmax number")
        quit()

def run(args):
    assert_usage(args)    
    max_number = int(args[1])
    total = 0
    print("Started")
    single_percent = max_number / 100
    prev_percentage = 0
    for prime in generate_primes():
        if prime == 1:
            continue # we don't consider 1 a prime in this problem
        
        percentage = int(prime / single_percent)
        if percentage > prev_percentage:
            print("%d%%"% percentage)
        prev_percentage = percentage        

        if prime >= max_number:
            break    
        total += prime
    
    print("Solution:", total)
