"""Determine if a binary search tree is valid.

https://leetcode.com/problems/validate-binary-search-tree/
"""

def f(root):
    """Determine if binary search tree is valid.

    This solution uses a recursive DFS approach.

    Time: O(n)
    Space: O(n)

    Parameters
    ----------
    root : TreeNode
        A binary search tree

    Returns
    -------
    bool
        True if the tree is a valid binary search tree, else false.

    Examples
    --------
    >>> f(TreeNode())
    True

    """

    def g(node, left, right):
        if not node:
            return True
        if not left < node.val < right:
            return False
        return g(node.left, left, node.val) and g(node.right, node.val, right)

    return g(root, float('-inf'), float('inf'))
