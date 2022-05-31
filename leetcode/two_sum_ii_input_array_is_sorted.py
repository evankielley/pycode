"""Find the indices of two numbers in a sorted array that add up to a particular sum.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

def f(nums, target):
    """Finds the indices (1-indexed) of two numbers in a list that add to a target.

    This solution uses an array-based two-pointers approach.

    Time: O(n)
    Space: O(1)

    Parameters
    ----------
    nums : list of int
        A list of integers sorted in non-decreasing order.
    target : int
        The target number for the two numbers to sum to.

    Returns
    -------
    list of int
        The 1-indexed indices of the two values in the list that sum to the target

    Raises
    ------
    ValueError
        Thrown if no two numbers in the list sum to the target.
    """
    l = 0
    r =  len(nums) - 1
    while l < r:
        sum_ = nums[l] + nums[r]
        if sum_ == target:
            return [l+1, r+1]
        elif sum_ < target:
            l += 1
        else:
            r -= 1
    raise ValueError(f'No two numbers add to target {target}.')
