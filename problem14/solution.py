
from copy import deepcopy

def next_collatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1

DEBUG =False

def debug(*msg):
    if DEBUG:
        print(*msg)

def run(args):
    # collatz_sequence = []
    # x = 13
    # while x != 1:
    #     collatz_sequence.append(x)
    #     x = next_collatz(x)
    
    # collatz_sequence += [1]
    # print(collatz_sequence)
    # -----------



    sequences = [[1]]
    current_level_sequences = [[1]]
    next_level_sequences = []

    # current_number = 1
    # candidates=set([1])
    # while current_number < 13:
    #     current_number = sorted(candidates)[0]
    #     candidates.remove(current_number)
    #     # print(next_candidate)
    #     candidates.add(2*current_number)
    #     uneven_reverse = (current_number - 1) / 3
    #     if uneven_reverse % 3 == 0:
    #         candidates.add(uneven_reverse)

    #     print(x)
    #     x+=1
    start_number_lengths = {}
    current_max_number = 0
    
    try:
        while current_max_number < 1e6:
            print("current max", current_max_number)
            for sequence in current_level_sequences:
                # even branch
                next_number1 = sequence[-1]*2
                if next_number1 < 1e6:
                    current_max_number = max(current_max_number, next_number1)
                sequence1 = sequence + [next_number1]
                next_level_sequences.append(sequence1)
                sequences.append(sequence1)
                start_number_lengths[sequence1[-1]] = max(start_number_lengths.get(sequence1[-1],0), len(sequence1))

                # uneven branch
                next_number2 = (sequence[-1] - 1) / 3
                if (int(next_number2) == next_number2) and next_number2 not in [0,1] :
                    if next_number2 < 1e6:
                        current_max_number = max(current_max_number, next_number2)

                    sequence2 = sequence + [int(next_number2)]
                    next_level_sequences.append(sequence2)
                    sequences.append(sequence2)
                    start_number_lengths[sequence2[-1]] = max(start_number_lengths.get(sequence2[-1],0), len(sequence2))
                
            current_level_sequences = deepcopy(next_level_sequences)
            next_level_sequences = []
    except KeyboardInterrupt:
        print("stopped")


    # except StopIteration:
    for sequence in sequences:
        print(sequence)
    
    print("-------")
    print(start_number_lengths)
    longest_length = 0
    start_number_longest = -1
    for (start_number, length) in start_number_lengths.items():
        if length > longest_length:
            longest_length = length
            start_number_longest = start_number



    print(start_number_longest, longest_length)
    print("CURRENT MAX", current_max_number)









# Collatz Sequence Generator

#  try:
#         while True:
#             for sequence in current_level_sequences:
#                 # even branch
#                 next_number1 = sequence[-1]*2
#                 sequence1 = sequence + [next_number1]
#                 next_level_sequences.append(sequence1)
#                 sequences.append(sequence1)
#                 start_number_lengths[sequence1[-1]] = max(start_number_lengths.get(sequence1[-1],0), len(sequence1))
#                 if sequence1[-1] > 1e6:
#                     raise StopIteration

#                 # uneven branch
#                 next_number2 = (sequence[-1] - 1) / 3
#                 if (int(next_number2) == next_number2) and next_number2 not in [0,1] :
#                     sequence2 = sequence + [int(next_number2)]
#                     next_level_sequences.append(sequence2)
#                     sequences.append(sequence2)
#                     start_number_lengths[sequence2[-1]] = max(start_number_lengths.get(sequence2[-1],0), len(sequence2))

#                     if sequence2[-1] > 1e6:
#                         raise StopIteration

                
#             current_level_sequences = next_level_sequences
#     except StopIteration:
#         for sequence in sequences:
#             print(sequence)
        
#         print("-------")
#         print(start_number_lengths)
#         longest_length = 0
#         start_number_longest = -1
#         for (start_number, length) in start_number_lengths.items():
#             if length > longest_length:
#                 longest_length = length
#                 start_number_longest = start_number