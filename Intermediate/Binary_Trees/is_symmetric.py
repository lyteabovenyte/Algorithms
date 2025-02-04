"""
    Design an algorithm which determines whether the input binary tree is symmetric or not.
    symmetric -> if you draw a vertical line from root the left and right side are the mirror of each
    other both structurally and in data.
"""
from BinaryTreeNode import BinaryTreeNode as N

def is_symmetric(tree):

    def check_symmetric(subtree0, subtree1):
        if not subtree0 and not subtree1:
            return True
        elif subtree0 and subtree1:
            return (subtree0.data == subtree1.data
                    and
                    check_symmetric(subtree0.left, subtree1.right)
                    and
                    check_symmetric(subtree0.right, subtree1.left))
        # at this point, one the subtrees are bigger.
        # means that one subtree is empty and the other one is not.
        return False
    return not tree or check_symmetric(tree.left, tree.right)



def my_dummy_sol(tree):
    left, right = tree.left, tree.right
    while left and right:
        left = left.left
        right = right.right

    if left is not None or right is not None:
        return False

    left_2, right_2 = tree.left, tree.right
    while left_2 and right_2:
        left_2 = left_2.right
        right_2 = right_2.left

    if left_2 is not None or right_2 is not None:
        return False

    return True


if __name__ == "__main__":
    example = N(1, N(2, N(3), None), N(2, None, N(3)))
    example2 = N(1, N(2, N(3), None), N(2, N(9), N(3)))
    print(is_symmetric(example))
    print(is_symmetric(example2))
    print(my_dummy_sol(example))
    print(my_dummy_sol(example2))