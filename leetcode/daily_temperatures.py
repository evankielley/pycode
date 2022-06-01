"""Determine the number of days until the next warmer day.

https://leetcode.com/problems/daily-temperatures/
"""

def f(temperatures):
    """Determine the number of days until the next warmer day.

    Parameters
    ----------
    temperatures : list of int
        A list of temperatures by day.

    Returns
    -------
    list of int
        A list of days until next warmer day.

    Examples
    --------
    >>> f([73,74,75,71,69,72,76,73])
    [1,1,4,2,1,1,0,0]

    """
    n = len(temperatures)
    days = [0 for _ in range(n)]
    stack = []
    for i, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            past_i = stack.pop()
            days[past_i] = i - past_i
        stack.append(i)
    return days
