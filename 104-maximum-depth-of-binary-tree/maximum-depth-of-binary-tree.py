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
        def recursive(root, max_depth, depth):
            if root.right == None and root.left == None:
                max_depth[0] = max(max_depth[0], depth)
                return 

            if root.left != None:
                recursive(root.left, max_depth, depth+1)
                print(max_depth, "root.left")

            if root.right != None:
                recursive(root.right, max_depth, depth+1)
                print(max_depth, "root.right")
        
        max_depth =[0]
        recursive(root, max_depth, 1)
        return max_depth[0]