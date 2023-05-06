# An interview question of finding the minimum operations

## Question

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: def minOperations(n)
- Returns an integer
- If n is impossible to achieve, return 0
  > > Example:
  > > n = 9
  > > H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

> > Number of operations: 6

## Solution

> > I solved this problem using prime factorization.
> > We keep dividing n by its smallest prime factor until n becomes 1. During each division, we add the prime factor to the total number of operations.
> > The reason this works is that any composite number can be factored into prime factors, and any sequence of copy and paste operations can be decomposed into a sequence of prime factors.
