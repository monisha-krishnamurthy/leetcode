from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = set()
        output = []
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            if level in levels:
                output[level] += node.val
            else:
                output.append(node.val)
                levels.add(level)
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        maximum = max(output)
        for level, out in enumerate(output):
            if out == maximum:
                return level+1

        