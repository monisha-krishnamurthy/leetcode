# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node, arr):
            if node is None:
                return None

            arr.append(node.val)

            dfs(node.left, arr)
            dfs(node.right, arr)
        
        dfs(root, arr)
        arr.sort()
        return arr[k-1]