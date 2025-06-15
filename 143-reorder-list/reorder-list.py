# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def recursive(root: ListNode, curr: ListNode) -> ListNode:
            if curr is None:
                return root

            root = recursive(root, curr.next)
            if root is None:
                return None

            temp = None
            if root == curr or root.next == curr:
                curr.next = None
            else:
                temp = root.next
                root.next = curr
                curr.next = temp 
            return temp

        recursive(head, head.next)



        