# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxv):
            if not root:
                return 0
                
            res = 1 if root.val >= maxv else 0
            maxv = max(maxv, root.val)
            
            res += dfs(root.left, maxv)
            res += dfs(root.right, maxv)

            return res
        
        return dfs(root, root.val)
