# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        print(length, "length")

        mid = length // 2
        print(mid, "mid")
        prev = None
        present = head
        for i in range(0, mid):
            prev = present
            present = present.next
        prev.next = present.next
        return head