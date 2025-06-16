# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        nodeToBeDeleted = length - n
        if nodeToBeDeleted == 0:
            return head.next

        count = 0
        current = head
        while current:
            count += 1
            if count == nodeToBeDeleted:
                current.next = current.next.next
                break
            current = current.next
        return head