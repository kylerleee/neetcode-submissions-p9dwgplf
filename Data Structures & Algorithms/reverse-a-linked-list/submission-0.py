# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        n = head
        val_list = []
        while n != None:
            val_list.append(n.val)
            n = n.next
            
        n = head
        x = ListNode(val_list.pop())
        new_head = x
        while n != None:
            if val_list:
                x.next = ListNode(val_list.pop())
            else:
                x.next = None
            n = n.next
            x = x.next
        return new_head