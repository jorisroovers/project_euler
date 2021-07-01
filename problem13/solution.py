
# Problem 13: Large sum
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# <See input.txt>

def assert_input(args):
    if len(args) != 2:
        msg = "Required Arguments\n"
        msg += "\t inputfile"
        quit(msg)

def run(args):
    assert_input(args)
    input_file = args[1]
    
    with open(input_file, 'r') as f:
        contents = f.readlines()
        total = 0
        for number_str in contents:
            print(int(number_str), total)
            total += int(number_str) 

    solution = str(total)[0:10]
    print("Solution:", solution)
