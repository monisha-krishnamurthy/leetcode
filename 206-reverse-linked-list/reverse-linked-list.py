# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = head
        if last is None:
            return last
        while True:
            if last.next != None:
                last = last.next
            else: 
                break

        prev = head
        while head.next != None:
            prev = head
            current = head.next        
            while current.next != None:
                prev = current
                current = current.next
            current.next = prev 
            prev.next = None
        head = last
        return head