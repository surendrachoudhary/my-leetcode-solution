# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dic = set()
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False 
            
            remain_value = k - node.val 
            if remain_value in dic:
                return True 
            
            dic.add(node.val)

            # Check left and right subtrees
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
