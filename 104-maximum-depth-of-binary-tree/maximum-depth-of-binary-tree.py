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
            if root.right == None and root.left == None:
                max_depth = max(max_depth, depth)
                return 

            if root.left != None:
                recursive(root.left, depth+1)
                print(max_depth, "root.left")

            if root.right != None:
                recursive(root.right, depth+1)
                print(max_depth, "root.right")

        recursive(root, 1)
        return max_depth