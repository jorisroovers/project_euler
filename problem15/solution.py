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
       # paths.append(current_path)
 
    return path_count 

if __name__ == "__main__":
     
    grid_size = int(sys.argv[1])
    for grid_size in xrange(1, grid_size+1):
        num_paths = follow_paths(0, 0, [], [], grid_size)
        print "Size %i, Solution: %s" % (grid_size, num_paths)
