# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_depth = 0 
        def recursive(root, depth):
            nonlocal max_depth
            if root== None:
                return 

            max_depth = max(max_depth, depth)
            recursive(root.left, depth+1)
            recursive(root.right, depth+1)

        recursive(root, 1)
        return max_depth