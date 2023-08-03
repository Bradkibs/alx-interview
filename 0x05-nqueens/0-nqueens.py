#!/usr/bin/python3
"""Backtracking algo solution for NQueens problem"""

import sys


class Nqueens:
    """A class containing the solution to the Nqueen problem"""
    def SolveNqueens(self, n):
        """Contains the solution method and all the core data and
        algorithms"""
        column = []
        positiveDiagonal = set()  # row + column is constant
        negativeDiagonal = set()  # row - column is constant
        row = []

        res = []

        def is_valid(r, c):
            """Checks if the current position is valid to place a queen"""
            return c not in column and (r + c) not in positiveDiagonal \
                and (r - c) not in negativeDiagonal

        def backtrack(r):
            """The backtracking algo that checks if
            the queen is already on that given row and
            positiveDiagonal or negativeDiagonal then
            discarding that position recursively"""
            if r == n:
                res.append([[row[i], column[i]] for i in range(n)])
                return

            for c in range(n):
                if is_valid(r, c):
                    column.append(c)
                    row.append(r)
                    positiveDiagonal.add(r + c)
                    negativeDiagonal.add(r - c)

                    backtrack(r + 1)

                    column.pop()
                    row.pop()
                    positiveDiagonal.remove(r + c)
                    negativeDiagonal.remove(r - c)

        backtrack(0)

        for solution in res:
            print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solution = Nqueens()
    if not sys.argv[1].isnumeric():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    solution.SolveNqueens(int(sys.argv[1]))
