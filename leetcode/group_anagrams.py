"""Group words from a list that are anagrams of each other into sublists.

https://leetcode.com/problems/group-anagrams/
"""

import collections

def f(words):
    """Group words from a list that are anagrams of each other into sublists.

    Time: O(nm), where n is the number of words and m is the average number of chars in a word.
    Space: O(n).

    Parameters
    ----------
    words : list of str
        A list of words.

    Returns
    -------
    list of list of str
        A list of lists of words that are anagrams of each other.

    Examples
    -------
    >>> f(["eat","tea","tan","ate","nat","bat"])
    [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    BASE_CHAR_VALUE = ord('a')
    anagrams_by_char_count_list = collections.defaultdict(list)
    for word in words:
        char_count_list = [0] * 26
        for char in word:
            char_count_list[ord(char) - BASE_CHAR_VALUE] += 1
        anagrams_by_char_count_list[tuple(char_count_list)].append(word)
    return list(anagrams_by_char_count_list.values())
