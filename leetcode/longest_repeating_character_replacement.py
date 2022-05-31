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
    check_is_valid = lambda l, r: r - l + 1 - max(hashmap.values()) <= k
    while r < n:
        hashmap[s[r]] = hashmap.get(s[r], 0) + 1
        while not check_is_valid(l, r):
            hashmap[s[l]] -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
        r += 1
    return max_len
