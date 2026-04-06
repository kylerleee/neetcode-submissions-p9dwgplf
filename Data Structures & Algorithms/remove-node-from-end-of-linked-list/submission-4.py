# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0
        curr = head
        curry = head
        while curry:
            count+=1
            curry = curry.next

        travel = count - n
        count = 0
        prev = None
        while curr: 
            temp = curr.next
            
            if count == travel:
                if travel != 0: 
                    prev.next = temp
                    curr.next = None
                else:
                    curr.next = None
                    return temp

            prev = curr
            curr = temp
            
            count+=1

        return head

