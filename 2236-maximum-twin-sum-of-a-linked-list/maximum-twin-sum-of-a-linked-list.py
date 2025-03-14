# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        max_arr = [0]* (length // 2)

        present = head
        mid = length // 2
        i = 0
        while present:
            if i >= 0 and i < mid:
                max_arr[i] = present.val
                # print(max_arr, "for first mid/2")
            if i >= mid and i < length:
                max_arr[length-1-i] += present.val
                # print(max_arr, "for later mid")
            i += 1
            present = present.next
        # print(max_arr)
        return max(max_arr)