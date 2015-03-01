# Starting in the top left corner of a 2×2 grid, and only being able to 
# move to the right and down, there are exactly 6 routes 
# to the bottom right corner.
import sys

def follow_paths(x, y, current_path, paths, grid_size):
    path_count = 0
    target_reached = True
    if x != grid_size:
        right_path = current_path[:]
        right_path.append('r')
        path_count += follow_paths(x+1, y, right_path, paths, grid_size)
        target_reached = False

    if y != grid_size:
        down_path = current_path[:]
        down_path.append('d')
        path_count += follow_paths(x, y+1, down_path, paths, grid_size)
        target_reached = False

    if target_reached:
        paths.append(current_path)
        path_count = 1

    return path_count

def combination(p, q):

    def fac(n):
        return 1 if n ==1 else n * fac(n-1)

    return fac(q)/(fac(q-p)*fac(p))


if __name__ == "__main__":
# The main insight for the solution to this problem is that each path that 
# reaches the bottom right corner has the following properties
# for grid size 2: [ 'D', 'R', 'D', 'R']
#   -> the length of each valid path is 4
#   -> in each path, there are 2 'D' movements, and 2 'R' movements
# for grid size n:
#   -> the length of each valid path is n*2
#   -> in each path, there are n 'D' movements, and n 'R' movements
# 
# So, what we are really looking for is what number of arrays of length n*2
# contain n 'D's and n 'R's.
# To generate a single such array, we randomly pick n positions for 'D' in 
# that array, and fill the positions that are not chosen with by 'R'.
# To determine how many such arrays we can generate, we fall back to a 
# basic combinatorial: choose n out of n*2 -> C(n, n*2)
# From math, we know that C(p, q) -> q!/(q-p)!p!

    grid_size = int(sys.argv[1])

    for grid_size in xrange(1, grid_size+1):
        paths = []
        #num_paths = follow_paths(0, 0,[], paths, grid_size)
        combinations = combination(grid_size, grid_size * 2)
        print "Size %i, Solution: %i" % (grid_size, combinations)
        #print paths

