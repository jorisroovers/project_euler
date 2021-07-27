
########################################################################################################################
# Problem 18: Largest palindrome product
########################################################################################################################

# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by
# brute force, and requires a clever method! ;o)
########################################################################################################################
# NOTES
# - The main insight is that you need to work bottoms up and for each triplet (parent, child1, child2), determine the
#   the maximum sum: Either parent+child1, or parent+child2, and store that value in the parent node. When you do this
#   recursively/iteratively towards the top, each node will contain the maximum sum that can be found in subtree for
#   which that node is the root. Note: you store this max_sum_subtree in the node, but you also keep the original value,
#   so each node becomes a tuple: (original value, max_sum_subtree).
# - To then find the path that contains the maximum sum, you just need to iterate the tree again but top-down and
#   follow the child that contains the largest max_sum_subtree. By summing the value of each node along the way, you'll
#   find the total maximum sum.
# - A more programatic part of this problem is determining the indices of child nodes in the 1D array containing all
#   data, given the index of the parent node.
#   For binary trees, you can easily solve this using a formula that only requires the parent index, but for
#   triangular/binomial trees (like here) that's not the case (some research seems to confirm this).
#   To calculate the child indices, you also need the row_number/depth of the tree:
#     child1_index = parent_index + depth
#     child2_index = parent_index + depth +1
#   
#   The only way to do this, is to construct an actual tree at startup time, incrementing the depth as you traverse the
#   tree and storing the child indices together with each parent node so they can easily be retrieved later.  
########################################################################################################################


from dataclasses import dataclass
import os

@dataclass
class TreeElement:
    tree: any
    val: int
    c1_index: int
    c2_index: int
    max_sum_subtree: int = None

    @property
    def c1(self):
        if self.c1_index:
            return self.tree.data[self.c1_index]
        return None

    @property
    def c2(self):
        if self.c2_index:
            return self.tree.data[self.c2_index]
        return None

class Tree:

    def __init__(self, data):
        self.data = []
        # Iterate through the data, for each element, determine child node indices based on current tree depth
        # and store all of that in a TreeElement
        depth = 1
        items_in_row = 0
        for i, d in enumerate(data):
            if items_in_row == depth: # in triangular trees, the number of nodes on each level equals |depth|
                depth += 1
                items_in_row = 0
            
            c1_index =  i + depth
            c2_index = i + depth + 1 

            # deal with leaf nodes
            c1_index = None if c1_index > len(data) - 1 else c1_index
            c2_index = None if c2_index > len(data) - 1 else c2_index

            self.data.append(TreeElement(tree=self, val=int(d), c1_index=c1_index, c2_index=c2_index))
            items_in_row+=1


    def __len__(self):
        return len(self.data)

    def get(self, i):
        return self.data[i]

def run(args):

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")

    numbers = []
    with open(input_file, 'r') as f:
        contents = f.read()
        numbers = contents.split()

    tree = Tree(numbers)

    # Iterate tree backwards (=bottoms up), for each node, determine the maximum sum of the subtree below
    for i in range(len(tree)-1, -1, -1):
        el = tree.get(i)
        
        # no children = leaf = max sum subtree = value of node itself
        if not el.c1:
            el.max_sum_subtree = el.val
        else:
            c1_sum = el.val + el.c1.max_sum_subtree
            c2_sum = el.val + el.c2.max_sum_subtree
            el.max_sum_subtree = max(c1_sum, c2_sum)
        
    # Traverse the tree top-down, following the largest max_sum_subtree
    max_sum = 0
    node = tree.get(0)
    while True:
        max_sum += node.val
        # stop iterating if we've reached the leaf nodes
        if node.c1 == None:
            break

        node = node.c1 if node.c1.max_sum_subtree > node.c2.max_sum_subtree else node.c2

    print("MAX SUM", max_sum)
