"""Find the length of the longest substring of repeating characters with at most k character replacements.

https://leetcode.com/problems/longest-repeating-character-replacement/
"""

def f(s, k):
    """Find the length of the longest substring of repeating characters with at most k character replacements.

    This solution uses a sliding window approach.

    Time: O(n), O(26n) which reduces to O(n)
    Space: O(n)

    Parameters
    ----------
    s : str
        A string.
    k : int
        The maximum number of character replacements allowed.

    Returns
    -------
    int
        The length of the longest substring of repeating characters with a most k character replacements.

    Examples
    --------
    >>> f("ABAB", 2)
    4

    """
    max_len = 0
    hashmap = dict()
    n = len(s)
    l = 0
    r = 0
    check_is_valid = lambda l, r: r - l + 1 - hashmap[max(hashmap, key=hashmap.get)] <= k
    while r < n:
        hashmap[s[r]] = hashmap.get(s[r], 0) + 1
        is_valid = check_is_valid(l, r)
        if is_valid:
            max_len = max(max_len, r - l + 1)
        else:
            while not is_valid and l < r:
                hashmap[s[l]] -= 1
                l += 1
                is_valid = check_is_valid(l, r)
        r += 1
    return max_len
