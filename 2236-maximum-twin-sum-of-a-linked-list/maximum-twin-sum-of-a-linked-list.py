# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        temp = head
        while temp != None:
            length +=1
            temp = temp.next
        
        map_twin = dict()
        max_sum = 0
        temp = head
        index = 0
        while temp != None:
            if length-index-1 in map_twin:
                map_twin[length-index-1] += temp.val
                max_sum = max(max_sum, map_twin[length-index-1])
            else:
                map_twin[index] = temp.val
            index +=1
            temp = temp.next
        return max_sum