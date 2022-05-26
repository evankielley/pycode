"""Determines if the values entered in a sudoku are valid.

https://leetcode.com/problems/valid-sudoku/
"""

import collections

def f(board, empty_value='.'):
    """Checks to see if a sudoku board has valid values.

    Time: O(81)
    Space: O(81)

    Parameters
    ----------
    board : list of list of int or str
        A sudoku board.
    empty_value : str, optional
        The value that is used in empty cells, by default '.'.

    Returns
    -------
    bool
        True is the sudoku board is valid, false otherwise.
    """
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)
    for i in range(9):
        for j in range(9):
            value = board[i][j]
            if value == empty_value:
                continue
            if value in rows[i]:
                return False
            if value in cols[j]:
                return False
            if value in squares[(i//3, j//3)]:
                return False
            rows[i].add(value)
            cols[j].add(value)
            squares[(i//3, j//3)].add(value)
    return True
