# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_inorder = {val : index for index, val in enumerate(inorder)}

        def buildTreeHelper(preorder, preStart, preEnd, inorder, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None 

            root = TreeNode(preorder[preStart])
            inRoot = hash_inorder[root.val]
            numsLeft = inRoot - inStart

            root.left = buildTreeHelper(preorder, preStart + 1, preEnd + numsLeft, inorder, inStart, inRoot - 1)
            root.right = buildTreeHelper(preorder, preStart + numsLeft +  1, preEnd, inorder, inRoot + 1, inEnd)

            return root 

        root = buildTreeHelper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        return root