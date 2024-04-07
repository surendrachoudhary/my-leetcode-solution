# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        rcMap = collections.defaultdict(list)

        def dfs(root, curRow, curCol):
            if root == None:
                return None 

            rcMap[curCol].append((curRow, root.val)) 
            left = dfs(root.left, curRow + 1, curCol - 1)
            right = dfs(root.right, curRow + 1, curCol + 1)
            

        dfs(root, 0,0)

        print(rcMap)
        
        ans = []
        

        for index in sorted(rcMap.keys()):
            final = sorted(rcMap[index], key=lambda x: (x[0], x[1]))
            ans.append([val[1] for val in final])

        return ans

            