

# CMPS 2200 Assignment 1

**Name:** __Cameron McLaren__


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not?
.  
.  No, 2^(n+1) is not in O(2^n) because if you plug in any value for n, 2^(n+1) will always output a larger value. While they both have exponential growth rate, 2^(n+1) grows quicker, therefore it's always going to have a slower time complexity than O(2^n).
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?
.  
.  No, 2^(2^n) is not in O(2^n) because of the same logic as above: if you plug in any value for n, 2^(2^n) will always output a larger value. While they both have exponential growth rate, 2^(2^n) grows quicker, therefore it's always going to have a slower time complexity than O(2^n).
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?
.  
.  No, n^(1.01) is not in O(log^2 n) because of the same logic as above: if you plug in any value for n, n^(1.01) will always output a larger value. n^(1.01) grows quicker since it's polynomial, therefore it's always going to have a slower time complexity than O(log^2 n), which is logarithmic.
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?
.  
.  Yes, n^(1.01) is in Omega(log^2 n) because if you plug in any value for n, n^(1.01) will always output a larger value. n^(1.01) grows quicker since it's polynomial, therefore it's always going to have a slower time complexity than Omega(log^2 n), which is logarithmic. Hence, with n^(1.01), it is greater than Omega(log^2 n) therefore it's above the lower bound set by the Omega function.
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?
.  
.  No, sqrt(n) is not in O((logn)^3) because if you plug in any value for n, sqrt(n) will always output a larger value. sqrt(n) grows quicker since it's a square root function, therefore it's always going to have a slower time complexity than O((logn)^3), which is logarithmic. Thus, sqrt(n) will always exceed the bound set by the Big-O function.
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?
.  
.  Yes, sqrt(n) is in Omega((logn)^3) because if you plug in any value for n, sqrt(n)) will always output a larger value. sqrt(n) grows quicker since it's a square root function, therefore it's always going to have a slower time complexity than Omega((logn)^3), which is logarithmic. Hence, with sqrt(n), it is greater than Omega((logn)^3) therefore it's above the lower bound set by the Omega function.
.
.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function takes in a value which represents the nth element in the Fibonacci sequence. If the number is 1 or 0, it simply returns that value since those are the corresponding Fibonacci sequence values. However, if the number is greater than 1, it calls the function foo recursively in order to add up the previous 2 numbers in the sequence (the method used for calculating each subsequent term in the Fibonacci sequence).
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?

.  The work of this function is O(n) because the amount of times the function iterates is dependent on the length of the list, since the for-loop in the function runs as many times as there are elements in the list. Since there's no parallelism in the iterative implementation of this function, the span is also O(n).
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  The base case has a work of O(1) because it's a simple comparison
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  
.  
.  
.  
.  
.  

