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
        # Initialize max_sum to negative infinity to ensure it gets updated during traversal
        self.max_sum = float('-inf')

        def max_path_sum_helper(node):
            if not node:
                return 0

            # Recursively calculate the maximum path sum for the left and right subtrees
            left_sum = max(max_path_sum_helper(node.left), 0)
            right_sum = max(max_path_sum_helper(node.right), 0)

            # Update the maximum path sum by considering the current node
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)

            # Return the maximum path sum considering only one side (either left or right, which one is maximum in value)
            return node.val + max(left_sum, right_sum)

        # Start the recursive traversal from the root
        max_path_sum_helper(root)

        return self.max_sum
