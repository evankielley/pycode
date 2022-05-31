"""Find all index-unique triplets that sum to zero.

https://leetcode.com/problems/3sum/
"""

def f(nums):
    """Find all index-unique triplets that sum to zero.

    This solution uses a two-pointer approach.

    Time: O(n^2)
    Space: O(n)

    Parameters
    ----------
    nums : list of int
        A list of integers

    Returns
    -------
    list of list of int
        A list of all index-unique triplets that sum to zero.

    Example
    -------
    >>> f([-1,0,1,2,-1,-4])
    [[-1,-1,2],[-1,0,1]]

    """
    triplets = []
    n = len(nums)
    nums.sort() # timsort: time O(nlogn), space O(n)
    prev = None
    for i, num1 in enumerate(nums):
        if num1 == prev:
            continue
        prev = num1
        l, r = i+1, n-1
        while l < r:
            num2, num3 = nums[l], nums[r]
            sum_ = num1 + num2 + num3
            if sum_ > 0:
                r -= 1
                continue
            if sum_ < 0:
                l += 1
                continue
            triplets.append([num1, num2, num3])
            prev_l = l
            l += 1
            while nums[prev_l] == nums[l] and l < r:
                l += 1
    return triplets
