from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  
        def recursive(node, node_search):
            if node is None: 
                return []
            if node.val == node_search.val:
                return [node]

            path2 =  []
            path1 = recursive(node.left, node_search)
            if len(path1)== 0:
                path2 = recursive(node.right, node_search) 
            if not path1 and not path2:
                return []
            else:
                return [node] + path1 + path2 

        out1 = recursive(root, p)
        out2 = recursive(root, q)
        while len(out1) < len(out2):
            out2.pop()
        while len(out2) < len(out1):
            out1.pop()
        
        while True:
            ele1 = out1.pop()
            ele2 = out2.pop()
            if ele1 == ele2:
                return ele1
