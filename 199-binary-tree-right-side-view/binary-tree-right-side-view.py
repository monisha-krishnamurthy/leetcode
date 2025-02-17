from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        out = defaultdict(list)
        levels = set()
        output = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            out[level].append(node.val)
            if level in levels:
                output[level] = node.val
            else:
                output.append(node.val)
                levels.add(level)
            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))
        return output
