

if __name__ == "__main__":
    
    with open('input.txt', 'r') as f:
        contents = f.readlines()
        total = 0
        for number_str in contents:
            print int(number_str), total
            total += int(number_str) 

    solution = str(total)[0:10]
    print "Solution:", solution
