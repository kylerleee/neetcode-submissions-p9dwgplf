# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.boo = True
        def dfs(root):
            if not root:
                return True

            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0
            
            if left is False or right is False:
                self.boo = False
            if abs(left-right) > 1:
                self.boo = False
            return max(left, right) + 1
        dfs(root)
        return self.boo
