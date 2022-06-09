"""Determine the number of car fleets that arrive at a destination.

https://leetcode.com/problems/car-fleet/
"""

def f(destination, positions, speeds):
    """Determine the number of car fleets that arrive at a destination.

    This approach uses sorting and a stack.

    Time: O(nlogn), sorting is O(nlogn) and processing is O(n).
    Space: O(n), creates a new array of positions and speeds as well as a stack.

    Parameters
    ----------
    destination : int
        The destination.
    positions : list of int
        The starting positions of the respective cars.
    speeds : list of int
        The speeds of the respective cars.

    Returns
    -------
    int
        The number of car fleets that arrive at the destination.

    Examples
    --------
    >>> f(12, [10,8,0,5,3], [2,4,1,1,3])
    3
    """
    cars = [(position, speed) for position, speed in zip(positions, speeds)]
    cars.sort(key=lambda x: x[0], reverse=True)
    stack = []
    prev_time = None
    for position, speed in cars:
        time = (destination - position) / speed
        if not stack or time > prev_time:
            stack.append(time)
            prev_time = time
    return len(stack)
