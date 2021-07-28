# Project Euler - Solutions
An attempt to solve the [Project Euler](http://projecteuler.net/) challenges. 

I do this purely for fun. My goal is mostly to solve the problem in reasonable compute time, not necessarily to come up
with the most elegant solution.

Code for each problem is located in the according directory (package) in a `solution.py` module.

To run the solution for a given problem:

```sh
python runner.py <problem nr> <problem args>

# Example
python runner.py 7 100
```

# Solutions
Problem Nr | Invocation for solution                                  | Solution
-----------|----------------------------------------------------------|-----------
1          | `python runner.py 1 1000`                                | 233168
2          | `python runner.py 2 4000000`                             | 4613732
3*         | `python runner.py 3 600851475143`                        | 6857
4          | `python runner.py 4`                                     | 906609
5          | `python runner.py 5 20`                                  | 232792560
6          | `python runner.py 6`                                     | 25164150 
7          | `python runner.py 7 10001`                               | 142913828922
8          | `python runner.py 8 13`                                  | 23514624000
9          | `python runner.py 9`                                     | 31875000
10         | `python runner.py 10 2000000`                            | 142913828922
11         | `python runner.py 11 problem11/input.txt`                | 104743
12         | `python runner.py 12`                                    | 76576500
13         | `python runner.py 13`                                    | 5537376230
14         | `python runner.py 14`                                    | 837799
15         | `python runner.py 15 20`                                 | 137846528820
16         | `python runner.py 16`                                    | 1366
17         | `python runner.py 17`                                    | 21124
18         | `python runner.py 18`                                    | 1074
19         | `python runner.py 19`                                    | 171
20         | `python runner.py 20 100`                                | 648
22         | `python runner.py 22`                                    | 871198282
24         | `python runner.py 24`                                    | 2783915460
25         | `python runner.py 25`                                    | 4782
67         | `python runner.py 18 problem67/p067_triangle.txt`        | 1074

# TODO
Some TODO items not related to the problems themselves, but to code cleanup/refactoring.

- Add default input options for run, so that you *can* run it without specifying the params: `DEFAULT_ARGS` module var?
