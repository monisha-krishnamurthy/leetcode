# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeArray = []
        current = head
        while current:
            nodeArray.append(current)
            current = current.next

        length = len(nodeArray)
        removeIndex = length - n
        
        if removeIndex == 0:
            return head.next

        nodeArray[removeIndex - 1].next = nodeArray[removeIndex].next
        return head 
