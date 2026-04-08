# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        def dft(root):
            left = dft(root.left) if root.left else "0"
            right = dft(root.right) if root.right else "0"

            return str(root.val) + left + right

        return dft(q) == dft(p)

