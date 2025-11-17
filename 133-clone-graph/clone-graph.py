"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        
        def clone_dfs(node):
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                if neighbor not in oldToNew:
                    copy.neighbors.append(clone_dfs(neighbor))
                else:
                    copy.neighbors.append(oldToNew[neighbor])
            return copy

        return clone_dfs(node) if node else None


