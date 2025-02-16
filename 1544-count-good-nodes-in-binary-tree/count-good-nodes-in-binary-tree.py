# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def recursive(root, max_value, good_nodes):
            if root is None:
                return 
            
            if root.val >= max_value:
                good_nodes[0] +=1
 
            recursive(root.left, max(max_value, root.val), good_nodes)
            print(good_nodes, "1st")

            recursive(root.right, max(max_value, root.val), good_nodes)
            print(good_nodes, "2nd")

        good_nodes = [0]
        recursive(root, float('-inf'), good_nodes)
        return good_nodes[0]