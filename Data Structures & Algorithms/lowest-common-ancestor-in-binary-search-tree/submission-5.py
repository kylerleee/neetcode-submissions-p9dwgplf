# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == root.val or q.val == root.val:
            return root
        head = root
        def dfs(root, find):
            if find.val < root.val:
                return [root.val] + dfs(root.left,find)
            elif find.val > root.val:
                return [root.val] + dfs(root.right,find)
            else:
                return [root.val]
        
        panc = dfs(root, p)[::-1]
        qanc = set(dfs(root, q))

        for i in range(len(panc)):
            if panc[i] in qanc:
                break 
            
        while True:
            if head.val < panc[i]:
                head = head.right
            elif head.val > panc[i]:
                head = head.left
            else:
                return head
        