# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current = head
        previous_node = None
        next_node = None
        while current:
            next_node = current.next
            current.next = previous_node
            previous_node = current
            current = next_node
        return previous_node

