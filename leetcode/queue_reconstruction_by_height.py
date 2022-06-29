def f(people):
    """Reconstruct array so that each person (h_i, k_i) has k_i people before them that are of height h_i or greater.

    Time: O(n^2), to loop over all people is O(n) and each insert is O(n).
    Space: O(n), sorting creates an additional array which is O(n) and we create an output array which is O(n).

    Parameters
    ----------
    people : list of list of int
        A misarranged list of people [[h_0, k_0], [h_1, k_1], ..., [h_n, k_n]] with heights (h_i) followed by the number of people in front of them with height greater than or equal to their own (k_i).

    Returns
    -------
    list of list of int
        A properly arranged list of people [[h_0, k_0], [h_1, k_1], ..., [h_n, k_n]] with heights (h_i) followed by the number of people in front of them with height greater than or equal to their own (k_i).

    Examples
    --------
    >>> f([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
    [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

    """
    people.sort(key=lambda x: (-x[0], x[1]))
    output = []
    for person in people:
        output.insert(person[1], person)
    return output
