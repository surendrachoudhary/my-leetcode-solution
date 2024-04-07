# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inMap = { val: index for index, val in enumerate(inorder)}

        def buildTreeHelper(postorder, poStart, poEnd, inorder, inStart, inEnd):
            if poStart > poEnd or inStart > inEnd:
                return None 
            root = TreeNode(postorder[poEnd])
            inRoot = inMap[root.val]
            leftNum = inRoot - inStart

            root.left = buildTreeHelper(postorder, poStart, poStart + leftNum -1, inorder, inStart, inRoot -1)
            root.right = buildTreeHelper(postorder, poStart + leftNum , poEnd - 1, inorder, inRoot + 1, inEnd)

            return root

        root = buildTreeHelper(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1)

        return root