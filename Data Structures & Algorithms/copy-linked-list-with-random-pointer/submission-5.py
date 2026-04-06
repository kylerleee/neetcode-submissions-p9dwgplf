"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}
        curr = head
        if not head:
            return head
        while curr:
            copy = Node(curr.val)
            dic[curr] = copy
            curr=curr.next
        
        curr=head
        while curr:
            copy = dic[curr]
            if curr.next == None:
                copy.next = None
            else:
                copy.next = dic[curr.next]
            if curr.random == None:
                copy.random = None
            else:
                copy.random = dic[curr.random]
            curr=curr.next

        return dic[head]