# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        out1 = []
        out2 = []

        def getLeafSeq(root):
            out = []
            stack = []
            stack.append(root)
            while stack:
                node = stack.pop()
                if node.left is None and node.right is None:
                    out.append(node.val)
                else:
                    if node.left is not None:
                        stack.append(node.left)
                    if node.right is not None:
                        stack.append(node.right)
            return out
    
        out1 = getLeafSeq(root1)
        out2 = getLeafSeq(root2)
        if out1 == out2:
            return True
        return False