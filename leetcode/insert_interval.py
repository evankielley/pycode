"""Insert an interval into a sorted list of intervals.

https://leetcode.com/problems/insert-interval/
"""

def f(intervals, new_interval):
    """Insert an interval into a sorted list of intervals.

    Time: O(n)
    Space: O(n)

    Parameters
    ----------
    intervals : list of list of int
        A sorted list of intervals [[start1, end1], [start2, end2], ...].
    new_interval : list of int
        The interval to add into the sorted list of intervals [start, end].

    Returns
    -------
    list of list of int
        A sorted list of intervals that includes the original list of intervals and the new interval.

    Examples
    --------
    >>> f([[1,3],[6,9]], [2,5])
    [[1, 5], [6, 9]]
 
    """
    output_intervals = []

    for i, interval in enumerate(intervals):
        if new_interval[1] < interval[0]:
            return output_intervals + [new_interval] + intervals[i:]
        if new_interval[0] > interval[1]:
            output_intervals.append(interval)
        else:
            new_interval = [min(new_interval[0], interval[0]), max(new_interval[1], interval[1])]

    return output_intervals + [new_interval]
