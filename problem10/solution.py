# Solution: 142913828922
from common.util import generate_primes

def assert_usage(args):
    if len(args) != 1:
        print "Required arguments"
        print "\tmax number"
        quit()

def run(args):
    assert_usage(args)    
    max_number = int(args[0])
    total = 0
    print "Started"
    single_percent = max_number / 100
    prev_percentage = 0
    for prime in generate_primes():
        if prime == 1:
            continue # we don't consider 1 a prime in this problem
        
        percentage = prime / single_percent
        if percentage > prev_percentage:
            print "%d%%"% percentage
        prev_percentage = percentage        

        if prime >= max_number:
            break    
        total += prime
    
    print "Solution:", total
