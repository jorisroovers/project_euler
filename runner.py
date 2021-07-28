import argparse
import sys
from common.util import LOG
import logging
import os

def print_usage():
    print("%s <problem nr> <param>*" % sys.argv[0])


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='Run the solution to an Euler Project problem')
    parser.add_argument('--debug', action='store_true', default=False, help='Print debug output')
    parser.add_argument('problem', type=int, help='Problem number to run')
    parser.add_argument('program args', nargs='*', help='Problem specific args')


    args = parser.parse_args()

    # Enable debugging
    if args.debug:
        LOG.setLevel(logging.DEBUG)

    # Dynamically import the selected problem package
    problem_nr = str(args.problem)
    if int(problem_nr) < 10 and problem_nr[0] != "0":
        problem_nr = "0" + problem_nr
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
    args = [sys.argv[0]] + sys.argv[2:]
    func(args)

