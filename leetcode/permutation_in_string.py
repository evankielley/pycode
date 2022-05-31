"""Determine if a string contains a permutation of another string.

https://leetcode.com/problems/permutation-in-string/
"""

def f(s1, s2):
    """Determine if a string contains a permutation of another string.

    Parameters
    ----------
    s1 : str
        The string to search for.
    s2 : str
        The string to search within.

    Returns
    -------
    bool
        True if the string contains a permutation of the other string, else false.

    Examples
    --------
    >>> f("ab", "eidbaooo")
    True
    """

    n1 = len(s1)
    n2 = len(s2)
    if n2 < n1:
        return False

    counter1 = dict()
    counter2 = dict()
    for i in range(ord('a'), ord('z') + 1):
        counter1[chr(i)] = 0
        counter2[chr(i)] = 0
    for i in range(n1):
        counter1[s1[i]] += 1
        counter2[s2[i]] += 1

    matches = 0
    for i in range(ord('a'), ord('z') + 1):
        if counter1[chr(i)] == counter2[chr(i)]:
            matches += 1

    for i in range(1, n2 - n1 + 1):

        cl = s2[i-1]
        counter2[cl] -= 1
        if counter1[cl] == counter2[cl]:
            matches += 1
        elif counter1[cl] == counter2[cl] + 1:
            matches -= 1

        cr = s2[i + n1 - 1]
        counter2[cr] += 1
        if counter1[cr] == counter2[cr]:
            matches += 1
        elif counter1[cr] == counter2[cr] - 1:
            matches -= 1

        if matches == 26:
            return True

    return matches == 26
