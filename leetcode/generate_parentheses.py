"""Generate all valid combinations of n pairs of parentheses.

https://leetcode.com/problems/generate-parentheses/
"""

def f(n):
    """Generate all valid combinations of n pairs of parentheses.

    This solution uses a BFS approach.

    Time: O(2^n)
    Space: O(2^n)

    Parameters
    ----------
    n : int
        The number of pairs of parentheses to generate.

    Returns
    -------
    list of str
        All valid combinations of n pairs of parenthesis.

    Examples
    --------
    >>> f(3)
    ["((()))","(()())","(())()","()(())","()()()"]

    """
    combos = []
    stack = [['(', 1, 0]]
    while stack:
        s, l, r = stack.pop()
        if l + r == n * 2:
            combos.append(s)
            continue
        if l < n:
            stack.append([s + '(', l + 1, r])
        if r < l:
            stack.append([s + ')', l, r + 1])
    return combos
