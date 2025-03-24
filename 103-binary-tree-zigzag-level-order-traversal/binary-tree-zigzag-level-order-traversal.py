# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        output = defaultdict(list)
        queue = deque()
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            output[level].append(node.val) 
 
            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))
        print(output)
        
        result = []
        for i in range(len(output)):
            if i%2 != 0:
                output[i] = output[i][::-1]
            result.append(output[i])
        print(result)
        return result