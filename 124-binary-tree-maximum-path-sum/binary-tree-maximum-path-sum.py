# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the result list to store the maximum path sum
        res = [float('-inf')]  # Initialize to negative infinity

        # Helper function to calculate the maximum path sum for a subtree
        def maxpsum(root):
            # Base case: If the current node is None, return 0
            if not root:
                return 0

            # Recursively calculate the maximum path sum for the left and right subtrees
            leftMax = max(maxpsum(root.left), 0)
            rightMax = max(maxpsum(root.right), 0)

            # Calculate the current path sum including the current node
            current_path_sum = root.val + leftMax + rightMax

            # Update the global maximum path sum using the current path sum
            res[0] = max(res[0], current_path_sum)

            # Return the maximum path sum considering only one side (either left or right)
            return root.val + max(leftMax, rightMax)

        # Start the recursive traversal from the root
        maxpsum(root)

        # Return the final result stored in the res list
        return res[0]
