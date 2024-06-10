# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
            
        idx = 0
        def helper(lower = float('-inf'), upper=float('inf')):
            nonlocal idx
            if idx == len(preorder):
                return None 

            val = preorder[idx]

            if val < lower or val > upper:
                return None 

            idx += 1
            rootNode = TreeNode(val)

            rootNode.left = helper(lower, val)
            rootNode.right = helper(val, upper)


            return rootNode

        return helper()
