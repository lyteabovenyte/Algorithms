"""
    Write a program which test if the input tree is height balanced or not.
    - height balanced tree is a tree which the difference between the height of the left and right subtree is
    at most one.
"""
import collections

def height_balanced_or_not(tree):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree): 
        if not tree:
            return BalancedStatusWithHeight(True, -1) # Base Case
        
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # Left subtree is not balanced
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height - right_result.height)
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced