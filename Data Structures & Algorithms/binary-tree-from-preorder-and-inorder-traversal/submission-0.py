# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        iodic = {}
        for i in range(len(inorder)):
            iodic[inorder[i]] = i
        
        self.idx = 0

        def dfs(l,r):
            if l > r:
                return None
            head = TreeNode(preorder[self.idx])
            mid = iodic[preorder[self.idx]]
            self.idx += 1
            

            head.left = dfs(l, mid - 1)
            head.right = dfs(mid + 1, r)
            return head
        return dfs(0, len(preorder) - 1)