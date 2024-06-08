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

        root = preorder[0]
        rootNode = TreeNode(root)

        rootLeft = []
        rootRight =   []

        for i in preorder[1:]:
            if root > i:
                rootLeft.append(i)
            elif root < i:
                rootRight.append(i)

        rootNode.left = self.bstFromPreorder(rootLeft)
        rootNode.right = self.bstFromPreorder(rootRight)
         
        return rootNode
