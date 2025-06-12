# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        
        current = head
        while current and stack:
            newData = stack.pop()
            current.val = newData
            current = current.next 
        return head