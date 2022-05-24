"""Determine the shortest length of time needed to process a list of tasks.

https://leetcode.com/problems/task-scheduler/
"""

import heapq
import collections

def f(tasks, n):
    """Determines the minimum amount of time that would be needed to complete a list of tasks.

    This solution uses a max heap and a queue to determine the task order that will take the least amount of time to process.

    Parameters
    ----------
    tasks : list of str
        A list of tasks by unique task identifier.
    n : int
        The time the CPU must wait before processing a task with the same identifier.

    Returns
    -------
    int
        The time needed to complete the entire list of tasks.
    """
    counter = collections.Counter(tasks)
    max_heap = [-count for count in counter.values()]
    heapq.heapify(max_heap) # negates to make a makeshift max heap
    queue = collections.deque()
    time = 0
    while max_heap or queue:
        time += 1
        if max_heap:
            count = heapq.heappop(max_heap)
            count += 1
            if count:
                queue.append((count, time + n))
        if queue:
            if queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
    return time
