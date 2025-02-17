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
        
        def getLeafSeqRecursive(root, output):
            if root.left is None and root.right is None:
                output.append(root.val)
                return
            
            if root.left is not None:
                getLeafSeqRecursive(root.left, output)
            if root.right is not None:
                getLeafSeqRecursive(root.right, output)

        getLeafSeqRecursive(root1, out1)
        getLeafSeqRecursive(root2, out2)
        if out1 == out2:
            return True
        return False