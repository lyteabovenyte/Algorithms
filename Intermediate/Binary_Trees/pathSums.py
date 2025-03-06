"""
    Design an algorithm which takes the root of a binary tree and returns 
    all the possible sums of the nodes from leaf to node.
"""

def pathSums(root):
    def dfs(root, current_sum, result):
        if not root:
            return
        
        current_sum += root.val
        
        if not root.left and not root.right:
            return current_sum
        
        dfs(root.left, current_sum, result)
        dfs(root.right, current_sum, result)

    result = []
    dfs(root, 0, result)
    return result