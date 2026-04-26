# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if abs(self.heightOfBinary(root.left) - self.heightOfBinary(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def heightOfBinary(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.heightOfBinary(root.left)
        right = self.heightOfBinary(root.right)

        return 1 + max(left,right)