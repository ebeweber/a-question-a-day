"""
Implement a function called is_balanced to check if a tree is balanced. For the
purposes of this question, a balanced tree is defined to be a tree such that no
two leaf nodes differ in distance from the root by more than one.
"""


class Node(object):
    """A very basic implementation of a binary tree"""

    def __init__(self, right=None, left=None):
        self.right = right
        self.left = left


def is_balanced(root):
    """Takes a tree (root node) and returns whether or not that tree is balanced

    :type root: Node
    :param root: the root node of the tree
    :rtype: bool
    :returns: whether or not the tree is balanced
    """
    root_min_and_max_depth = min_and_max_depth(root)
    return root_min_and_max_depth[1] - root_min_and_max_depth[0] <= 1


def min_and_max_depth(node):
    """Takes a node and returns the min and max depth between that node and any
    of its children.

    :type node: Node
    :param node: a tree node with children
    :rtype: tuple(int, int)
    :returns: the (min, max) depth corresponding to that node
    """
    if not node:
        return (0, 0)

    left_min_and_max_depth = min_and_max_depth(node.left)
    right_min_and_max_depth = min_and_max_depth(node.right)

    return (
        min(left_min_and_max_depth[0], right_min_and_max_depth[0]) + 1,
        max(left_min_and_max_depth[1], right_min_and_max_depth[1]) + 1
    )


# Tests
# TODO(matthewe|2014-07-23): May be worth eventually moving this to it's
# own file w/ pytest
tree1 = Node()
assert is_balanced(tree1)

tree2 = Node(
    left=Node(
        left=Node(
            left=Node(
                left=Node(
                    left=Node()
                )
            ),
            right=Node()
        )
    ),
    right=Node()
)
assert not is_balanced(tree2)
