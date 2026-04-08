# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if (not root and subRoot) or (not subRoot and root):
            return False

        if root and subRoot and root.val == subRoot.val and (root.left.val if root.left else None) == (subRoot.left.val if subRoot.left else None) and (root.right.val if root.right else None) == (subRoot.right.val if subRoot.right else None):
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                
        
