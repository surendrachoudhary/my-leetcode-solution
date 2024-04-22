# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Define a depth-first search (DFS) function to traverse the tree
        def dfs(root):
            # Base case: if the root is None, return 0
            if root == None:
                return 0

            # Recursively calculate the depths of the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # If the current node is a leaf node, return 1
            if root.left is None and root.right is None:
                return 1
            
            # If the current node has no right child, return the depth of the left subtree plus 1
            if root.right is None:
                return left + 1

            # If the current node has no left child, return the depth of the right subtree plus 1
            if root.left is None:
                return right + 1

            # Otherwise, return the minimum depth of the left and right subtrees plus 1
            return min(left, right) + 1

        # Start the DFS traversal from the root node
        return dfs(root)
