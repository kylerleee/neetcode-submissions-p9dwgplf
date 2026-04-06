# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = new = ListNode()
        
        while l1 or l2:
            li1 = l1.val if l1 else 0
            li2 = l2.val if l2 else 0
            if li1 + li2 + carry >= 10:
                r = (li1 + li2 + carry) % 10
                carry = 1
            else: 
                r = (li1 + li2 + carry)
                carry = 0
            new.next = ListNode(r)
            new = new.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            new.next = ListNode(1)
        
        return head.next