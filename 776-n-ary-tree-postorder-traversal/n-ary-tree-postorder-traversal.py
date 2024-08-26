"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def helper(root):
            if root is None:
                return 

            for c in root.children:
                helper(c)
            ans.append(root.val)
        
        helper(root)
        return ans 