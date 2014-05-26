import sys
import os
import problem1

def print_usage():
    print "%s <problem nr> <param>*" % sys.argv[0]

def assert_usage():
    if len(sys.argv) < 2:
        print_usage()
        quit()

if __name__ == "__main__":
    assert_usage()
    
    # Dynamically import the selected problem package
    problem_nr = sys.argv[1]
    problem_package_name =  "problem" + problem_nr
    if not os.path.exists(problem_package_name):
        quit("No such package: '%s'" % problem_package_name)
    
    module_name = "%s.solution" % problem_package_name
    function_name = "run"
    problem_module = __import__(module_name, fromlist=[function_name])
    if not hasattr(problem_module, function_name):
       quit("The module '%s.%s' has no function %s" % (problem_package_name, 
                                                       module_name, 
                                                       function_name))

    func = getattr(problem_module, function_name)
    func(sys.argv[2:])

