# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def ll_length(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     length = 0
    #     temp = head
    #     while temp:
    #         length +=1
    #         temp = temp.next
    #     return length 

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next

        return head
        # leng = self.ll_length(head)
        # temp = head
        # prev = None

        # for _ in range(leng//2):
        #     prev = temp
        #     temp = temp.next
        
        # if prev:
        #     prev.next = temp.next

        # return head