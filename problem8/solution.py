

if __name__ == "__main__":
  
    with open('input.txt', 'r') as f:
        contents = f.readlines()
        # input file as single str
        number_str = "".join(contents).replace("\n", "")
        
        number_str = "1234567890"
        i = 0
        window_size = 5
        last_window_start_index = len(number_str) - window_size
        largest_product = 0
        while i <= last_window_start_index:
            window = number_str[i:i+5]
            product = reduce(lambda x, y: int(x) * int(y), window)
            if product > largest_product:
                largest_product = product
            i += 1
        
        print "Solution: ", largest_product

