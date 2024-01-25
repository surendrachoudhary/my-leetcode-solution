# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.array =  []
        def inordertraversal(node):
            if not node:
                return 
            
            inordertraversal(node.left)
            self.array.append(node.val)
            inordertraversal(node.right)
        inordertraversal(root)

        self.start, self.end = 0, len(self.array)

    def next(self) -> int:
        self.start += 1
        return self.array[self.start-1]

    def hasNext(self) -> bool:
        return self.start < self.end


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()