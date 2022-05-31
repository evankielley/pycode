"""Get the k most frequent elements in a list.

https://leetcode.com/problems/top-k-frequent-elements/
"""

import heapq

def f(nums, k, solver='bucket_sort'):
    """Get the k most frequent elements in a list.

    Parameters
    ----------
    nums : list of int or float
        A list of numbers.
    k : int
        The number of most frequent elements to return.
    solver : str, optional
        The solver to use to obtain the solution, by default 'bucket_sort'.

    Returns
    -------
    list of int or float
        The k most frequent elements in the list.

    Raises
    ------
    NotImplementedError
        Raises this error if the solver specified is not recognized.

    Examples
    -------
    >>> f([1,1,1,2,2,3], 2)
    [1,2]
    """
    solver_map = {
        'bucket_sort': _bucket_sort_solver,
        'heap': _heap_solver,
    }
    if not solver in solver_map:
        raise NotImplementedError(f'Unrecognized solver: {solver}. Must be one of {list(solver_map.keys())}')
    return solver_map[solver](nums, k)

def _bucket_sort_solver(nums, k):
    """Get the k most frequent elements in a list by using a reverse bucket sort algorithm.

    Time: O(n)
    Space: O(n)

    Parameters
    ----------
    nums : list of int or float
        A list of numbers.
    k : int
        The number of most frequent elements to return.

    Returns
    -------
    list of int or float
        The k most frequent elements in the list.
    """
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    arr = [[] for _ in range(len(nums))]
    for num, count in counter.items():
        arr[count-1].append(num)
    output = []
    for _nums in arr[::-1]:
        if len(output) == k:
            break
        if len(_nums) > 0:
            output += _nums
    return output

def _heap_solver(nums, k):
    """Get the k most frequent elements in a list by using a max heap.

    Time: O(nlogn)
    Space: O(n)

    Parameters
    ----------
    nums : list of int or float
        A list of numbers.
    k : int
        The number of most frequent elements to return.

    Returns
    -------
    list of int or float
        The k most frequent elements in the list.
    """
    counter = dict()
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    hashmap = dict()
    for num, count in counter.items():
        hashmap[count] = hashmap.get(count, []) + [num]
    max_heap = [(-count, _nums) for count, _nums in hashmap.items()]
    heapq.heapify(max_heap)
    output = []
    while len(output) < k:
        output += heapq.heappop(max_heap)[1]
    return output
