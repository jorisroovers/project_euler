# Project Euler - Solutions
An attempt to solve the [Project Euler](http://projecteuler.net/) challenges. 

My goal is mostly to solve the problem in reasonable compute time, not necessarily to come up with the most elegant solution. 

Code for each problem is located in the according directory (package) in a `solution.py` module.

To run the solution for a given problem:

```sh
python runner.py <problem nr> <problem args>

# Example
python runner.py 7 100
```

NOTE: Currently still in the progress of converting the solutions to using
runner.py. For some you might need to run the directly:
```sh
cd problemx
python solution.py
```
# Solutions
Problem Nr | Invocation for solution                   | Solution
-----------|-------------------------------------------|-----------
1          | `python runner.py 1 1000`                 | 233168
2          | `python runner.py 2 4000000`              | 4613732
3*         | `python runner.py 3 600851475143`         | 6857
4          | `python runner.py 4`                      | 906609
5          | `python runner.py 5 20`                   | 232792560
6          | `python runner.py 6`                      | 25164150 
7          | `python runner.py 7 10001`                | 142913828922
8          | `python runner.py 8 13`                   | 23514624000
9          | `python runner.py 9`                      | 31875000
10         | `python runner.py 10 2000000`             | 142913828922
11         | `python runner.py 11 problem11/input.txt` | 104743
12         | `python runner.py 12`                     | 76576500
13         | `python runner.py 13`                     | 5537376230
14         | `python runner.py 14`                     | 837799
15         | `python runner.py 15`                     | 137846528820
16         | `python runner.py 16`                     | Not Finished
19         | `python runner.py 19`                     | 171
20         | `python problem20/solution.py 100`        | 648


# TODO
Some TODO items not related to the problems themselves, but to code cleanup/refactoring.

- Convert all problems to run using `runner.py` in python 3
- Add problem description to each problem in same formatting
- Add debug option to `runner.py` and debug logging
