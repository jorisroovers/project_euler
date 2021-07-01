
def assert_input(args):
    print(args)
    if len(args) != 2:
        msg = "Required Arguments\n"
        msg += "\t inputfile"
        quit(msg)

def run(args):
    assert_input(args)
    input_file = args[1]
    with open(input_file) as f:
        contents = f.readlines()
        print(contents)

        # # Convert text input file to matrix of numbers
        # horizontal = []
        # for line in contents:
        #     row = []
        #     line = line.rstrip("\n")
        #     horizontal.append([int(i) for i in line.split(" ")])
      
        # # Transpose matrix to get vertical direction 
        # vertical = []
        # for rowindex, row in enumerate(horizontal):
        #     for colindex, number in enumerate(row):
        #         if rowindex == 0:
        #             vertical.append([])
        #         vertical[colindex].append(number)
        #         #print index, number
        # #print vertical                
    
        # # Diagonal matrix (not done  yet)
        # diagonal = []
        # for rowindex, row in enumerate(horizontal):
        #     for colindex, number in enumerate(row):
        #         current_diag = None
        #         if rowindex == 0 or colindex < rowindex:
        #             current_diag = []
        #             diagonal.append(current_diag)
        #         else:
        #             diag_index = colindex + rowindex
        #             current_diag = diagonal[diag_index]
        #         current_diag.append(number)

        # for diag in diagonal:
        #     print diag



       
            

