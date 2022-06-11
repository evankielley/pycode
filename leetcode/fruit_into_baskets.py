"""Determine the maximum number of fruits that can be gathered.

https://leetcode.com/problems/fruit-into-baskets/
"""

def f(fruits):
    """Determine the maximum number of fruits that can be gathered.

    Time: O(n)
    Space: O(1)

    Parameters
    ----------
    fruits : list of int
        The type of fruit on each tree.

    Returns
    -------
    int
        The maximum number of fruits that can be gathered.

    Examples
    --------
    >>> f([1,2,1])
    3
    """
    n = len(fruits)
    if n < 2:
        return n
    basket = {}
    max_count = 0
    count = 0
    l = 0
    for fruit in fruits:
        basket[fruit] = basket.get(fruit, 0) + 1
        count += 1
        while len(basket.keys()) > 2:
            basket[fruits[l]] -= 1
            count -= 1
            if basket[fruits[l]] == 0:
                del basket[fruits[l]]
            l += 1
        if count > max_count:
            max_count = count
    return max_count
