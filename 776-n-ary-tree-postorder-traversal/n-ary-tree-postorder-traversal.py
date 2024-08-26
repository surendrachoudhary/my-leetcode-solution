"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        #iterative way after recursive 
        ans = []

        if root is None:
            return []

        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                ans.append(node.val)
            else:
                stack.append((node, True))
                for c in node.children[::-1]:
                    stack.append((c, False))
       
        return ans 