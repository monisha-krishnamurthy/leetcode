# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedArray = []

        current = list1
        while current:
            value = current.val
            mergedArray.append(value)
            current = current.next

        present = list2
        while present:
            value = present.val
            mergedArray.append(value)
            present = present.next
        print(mergedArray)
        
        if len(mergedArray) == 0:
            return None
            
        mergedArray.sort()   
        head = ListNode(mergedArray[0])
        temp = head
        for k in range(1, len(mergedArray)):
            temp.next = ListNode(mergedArray[k])
            temp = temp.next
        return head