"""Get the length of the longest consecutive sequence of an unsorted list of integers.

https://leetcode.com/problems/longest-consecutive-sequence/
"""

def f(nums):
    """Get the length of the longest consecutive sequence of an unsorted list of integers.

    Time: O(n)
    Space: O(n)

    Parameters
    ----------
    nums : list of int
        An unsorted list of integers.

    Returns
    -------
    int
        The length of the longest consecutive sequence.

    Examples
    -------
    >>> f([100,4,200,1,3,2])
    4
    """
    numset = set(nums)
    visited = set()
    longest_len = 0
    for num in nums:
        if num in visited:
            continue
        if num - 1 in numset:
            continue
        curr_len = 1
        while num + 1 in numset:
            visited.add(num)
            curr_len += 1
            num += 1
        longest_len = max(longest_len, curr_len)
    return longest_len
