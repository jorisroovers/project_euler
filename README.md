# Project Euler - Solutions
An attempt to solve the project Euler challenges.

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

# Not working
The following solutions are known to be incorrect:
- problem8

# Solutions
Problem Nr | Invocation for solution                   | Solution
-----------|-------------------------------------------|-----------
1          | `python runner.py 1 1000`                 | 233168
2          | `python runner.py 2 4000000`              | 4613732
3          | `python runner.py 3`                      | 6857
4          | `python problem4/solution.py`             | 906609
5          | `python problem5/solution.py 20`          | 232792560
6          | `python problem6/solution.py`             | 25164150 
7          | `python runner.py 7 10001`                | 142913828922
9          | `python runner.py 9`                      | 31875000
10         | `python runner.py 10 2000000`             | 142913828922
11         | `python runner.py 11 problem11/input.txt` | 104743
12         | `python runner.py 12`                     | 76576500
20         | `python problem20/solution.py 100`        | 648

