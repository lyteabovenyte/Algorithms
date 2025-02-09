"""
    Design an algorithm which returns the maximum pathSum in the tree.
"""

def max_path_sum(root):
    result = []
    
    def dfs(node, path):
        if not node:
            return [] 
        
        path.append(node.val)
        result.append(list(path))
        # if sum(path) > max([sum(ele) for ele in result]):
        #     result.append(list(path))

        dfs(node.left, path)
        dfs(node.right, path)

        # Backtrack
        path.pop()
    
        return max([sum(ele) for ele in result])
    
    return dfs(root, [])

