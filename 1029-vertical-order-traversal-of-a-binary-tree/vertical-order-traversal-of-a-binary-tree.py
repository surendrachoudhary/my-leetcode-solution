# Define the Solution class for vertical traversal of a binary tree
class Solution:
    # Method to perform vertical traversal
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Create a defaultdict to store nodes at each column
        rcMap = collections.defaultdict(list)

        # Depth-first search function to traverse the tree and populate the defaultdict
        def dfs(root, curRow, curCol):
            # Base case: return if the current node is None
            if root == None:
                return None 

            # Append the current node's row and value to the column map
            rcMap[curCol].append((curRow, root.val)) 
            
            # Recursively traverse the left and right subtrees
            left = dfs(root.left, curRow + 1, curCol - 1)
            right = dfs(root.right, curRow + 1, curCol + 1)

        # Start the depth-first search from the root at row 0 and column 0
        dfs(root, 0, 0)

        # Print the column map for debugging purposes
        print(rcMap)
        
        # Initialize the final answer list
        ans = []

        # Sort the column map keys and process each column
        for index in sorted(rcMap.keys()):
            # Sort the nodes in the current column based on row and value
            final = sorted(rcMap[index], key=lambda x: (x[0], x[1]))
            # Extract only the values from the sorted nodes and append them to the answer list
            ans.append([val[1] for val in final])

        # Return the final answer list
        return ans
