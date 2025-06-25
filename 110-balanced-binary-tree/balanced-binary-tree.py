# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0

        checker = 1
        lheight = self.check(root.left)
        if lheight == -1: return -1
        rheight = self.check(root.right)
        if rheight == -1: return -1
        
        if abs(lheight - rheight) > 1:
                return -1
        else:
            return max(lheight,rheight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root) != -1