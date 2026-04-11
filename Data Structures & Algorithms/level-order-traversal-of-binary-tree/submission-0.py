# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        visited = []
        q = []

        q.append(root)

        while q:
            qlen = len(q)
            res = []
            for i in range(qlen):
                next = q.pop(0)
                res.append(next.val)
                if next.left:
                    q.append(next.left)
                if next.right:
                    q.append(next.right)
            visited.append(res)
            

        return(visited)


        