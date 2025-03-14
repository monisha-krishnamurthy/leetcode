# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_head = l1
        l2_head = l2
        l1, l2 = '', ''
        while l1_head:
            l1 = str(l1_head.val) + l1
            l1_head = l1_head.next
        # print(l1)
        while l2_head:
            l2 = str(l2_head.val) + l2
            l2_head = l2_head.next
        # print(l2)
        result = int(l1) + int(l2)
        # print(result)

        head = None
        tail = None
        for digit in reversed(str(result)):
            new_node = ListNode(int(digit))
            if not head:
                head = new_node
                tail = head
            else:
                tail.next = new_node
                tail = new_node 
        return head