# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""
        q = deque()
        q.append(root)
        data = ""
        while q:
            node = q.popleft()
            if node and node != "#":
                data += str(node.val) + ","

                if node.left:
                    q.append(node.left)
                else:
                    q.append("#")

                if node.right:
                    q.append(node.right)
                else:
                    q.append("#")
            else:
                data += "#,"

        return data
                    


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None 

        q = deque()
        tokens = data.split(",")
        
        root_val = int(tokens.pop(0))
        root = TreeNode(root_val)
        q.append(root)

        while q:
            node = q.popleft()

            left_val = tokens.pop(0)

            if left_val != "#":
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)
            
            right_val = tokens.pop(0)

            if right_val != "#":
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))