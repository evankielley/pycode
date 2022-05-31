"""Find the length of the longest substring of a given string without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

def f(s):
    """Find the length of the longest substring of a given string without repeating characters.

    This approach uses a sliding window.

    Time: O(n)
    Space: O(n)

    Parameters
    ----------
    s : str
        The string to find the length of the longest substring of.

    Returns
    -------
    int
        The length of the longest substring of the given string without repeating characters.

    Examples
    --------
    >>> f("abcabcbb")
    3

    """
    n = len(s)
    l = 0
    r = 0
    hashset = set()
    max_len = 0
    while r < n:
        if not s[r] in hashset:
            hashset.add(s[r])
            max_len = max(max_len, r - l + 1)
        else:
            while not s[l] == s[r] and l < r:
                hashset.remove(s[l])
                l += 1
            l += 1
        r += 1
    return max_len
