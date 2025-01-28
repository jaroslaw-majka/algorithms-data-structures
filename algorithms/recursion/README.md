# Overview
Recursion is core concept in programming and algorithms. It utilizes stack concept to solve problem. 
Stack is a queue, where last object in is first out (LIFO), different from "normal" queue where first in is first out.

## Example
One of the most often used examples when thinking about recursion is factorial function.
```python
def factorial(n: int):
    if n == 1: # Base case
        return 1
    return n * factorial(n-1)
```
Each recursive function must have so-called 'Base case', a case in which the function stops going deeper and deeper into the cases. In above example 'Base case' is `if n == 1`.
Let's say we invoke the function `factorial(4)`
```python
# First invoke
n = 4 # so our base case is not met, 
return 4 * factorial(3)
# Second invoke
n = 3 # so again base case is not met, 
return 3 * factorial(2)
# Third invoke
n = 2 # base case not met, 
return 2 * factorial(1)
# Fourth invoke
n = 1 # base case met,
return 1

# NOW go back to Third invoke, 
# return was 2 * factorial(1), but factorial(1) returned 1, so function will calculate 2 * 1 and return 2
# Go back to Second invoke
# factorial(2) = 2, so 3 * 2 return 6
# Go back to First invoke
# factorial(3) = 6, so 4 * 6 return 24
# End the recursive function
```
The recursive function will first go into the max depth until it reaches the base case, and then will go back in LIFO (last in, first out) order.

## Currently covered algorithms

* Euclidean algorithm for calculating `a` to the power of `b`: [`euclidean.py`](/algorithms/recursion/euclidean.py)