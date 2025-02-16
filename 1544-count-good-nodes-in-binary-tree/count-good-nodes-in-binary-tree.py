# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0
        def recursive(root, max_value):
            nonlocal good_nodes
            if root is None:
                return 
            
            if root.val >= max_value:
                good_nodes +=1
 
            recursive(root.left, max(max_value, root.val))
            recursive(root.right, max(max_value, root.val))

        recursive(root, float('-inf'))
        return good_nodes