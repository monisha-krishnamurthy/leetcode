# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        lh = self.height(node.left)
        rh = self.height(node.right)
        return max(lh, rh) + 1

    def printKNodes(self, node: Optional[TreeNode], h: int, level: List[TreeNode]) -> List[TreeNode]:
        if node is None:
            return
        
        if h == 0:
            level.append(node.val)
        else:
            self.printKNodes(node.left, h-1, level)
            self.printKNodes(node.right, h-1, level)
        return level 

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        heightOfTree = self.height(root)
        res = []

        for i in range(heightOfTree):
            level = []
            self.printKNodes(root, i, level)
            res.append(level)
        return res



    