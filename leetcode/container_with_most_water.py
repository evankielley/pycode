"""Find the maximum area that can be filled with a fluid.

https://leetcode.com/problems/container-with-most-water/
"""

def f(heights):
    """Find the maximum area that can be filled with a fluid.

    This solution uses a two-pointer approach.

    Time: O(n)
    Space: O(1)

    Parameters
    ----------
    heights : list of int
        The heights of the walls.

    Returns
    -------
    int
        The maximum area that can be filled with a fluid.

    Example
    -------
    >>> f([1,8,6,2,5,4,8,3,7])
    49

    """

    n = len(heights)
    l = 0
    r = n-1
    max_area = 0
    while l < r:
        max_area = max(max_area, (r - l) * min(heights[l], heights[r]))
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return max_area
