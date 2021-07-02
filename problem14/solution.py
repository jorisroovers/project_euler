# Problem 14: Longest Collatz sequence
# 
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def next_collatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1

DEBUG =False

def debug(*msg):
    if DEBUG:
        print(*msg)


def run(n):
    sequences = {}
    for i in range(2, int(1e6)):
        if i % 1e4 ==0:
            print(i)
        n = i
        sequences[i] = []
        counter = 0
        while n != 1 or counter == 1000:
            sequences[i].append(n)
            n = next_collatz(n)
            counter += 1
        sequences[i].append(1)


        if counter == 1000:
            sequences[i] = []


    max_len = 0
    longest_i = 0
    for (i, sequence) in sequences.items():
        if len(sequence) > max_len:
            max_len = len(sequence)
            longest_i = i

    print("LONGEST", longest_i, max_len)
