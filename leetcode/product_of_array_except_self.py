"""Return an array of products of all elements except that at each index.

https://leetcode.com/problems/product-of-array-except-self/
"""

def f(nums):
    """Return an array of products of all elements except that at each index.

    This approach uses two additional arrays that compute the product before and after each index then combine those products.

    Time: O(n)
    Space: O(n)

    Parameters
    ----------
    nums : list of int
        A list of integers.

    Returns
    -------
    list of int
        A list of integers that are products of all elements in the array except that at its index.

    Example
    -------
    >>> f([1,2,3,4])
    [24,12,8,6]
    """
    n = len(nums)
    prods_before = [None for _ in range(n)]
    prods_after = [None for _ in range(n)]
    output = [None for _ in range(n)]
    prods_before[0] = 1
    prods_after[-1] = 1
    for i in range(1, n):
        prods_before[i] = prods_before[i-1] * nums[i-1]
    for i in range(n-2, -1, -1):
        prods_after[i] = prods_after[i+1] * nums[i+1]
    for i in range(n):
        output[i] = prods_before[i] * prods_after[i]
    return output
