"""Determine if cards can be arranged into groups of straights.

https://leetcode.com/problems/hand-of-straights/
"""

import collections
import heapq

def f(hand, group_size):
    """A greedy algorithm that uses a min heap to determine if cards can be arranged into groups of straights.

    Time: O(nlogn), pops from a min heap n times.
    Space: O(n), uses a counter dictionary and a min heap.

    Parameters
    ----------
    hand : list of int
        The cards values in the hand.
    group_size : int
        The group size

    Returns
    -------
    bool
        True if the cards can be arranged into groups of straights, else false.

    Example
    -------
    >>> f([1,2,3,6,2,3,4,7,8], 3)
    True
    """
    if len(hand) % group_size:
        return False
    counter = collections.Counter(hand)
    min_heap = list(counter.keys())
    heapq.heapify(min_heap)
    while min_heap:
        min_num = min_heap[0]
        if counter[min_num] == 0:
            heapq.heappop(min_heap) # O(logn) time
            continue
        else:
            for num in range(min_num, min_num + group_size):
                if not counter.get(num, 0) > 0:
                    return False
                counter[num] -= 1
    return True
