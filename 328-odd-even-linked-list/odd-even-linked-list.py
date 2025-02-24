# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        temp = head.next
        while True:
            odd.next = even.next
            if odd.next is None:
                odd.next = temp
                break
            odd = odd.next
            even.next = odd.next
            if even.next is None:
                odd.next = temp
                break
            even = even.next
        
        return head
        
            
