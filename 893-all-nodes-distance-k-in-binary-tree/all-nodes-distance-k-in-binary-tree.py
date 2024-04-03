# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_hash = collections.defaultdict(int) 
        def parent_connect(root):
            q = deque()
            q.append(root)

            while q:
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    parent_hash[node.left] = node
                if node.right:
                    q.append(node.right)
                    parent_hash[node.right] = node
        
        parent_connect(root)

        
        def find_distance(target,k):
            visited_node = set()
            q = deque()
            q.append(target)
            visited_node.add(target)

            curr_level = 0

            while q:
                
                size = len(q)
                
                if curr_level == k:
                    break

                for _ in range(size):
                    curr_node = q.popleft()

                    if curr_node.left and curr_node.left not in visited_node:
                        q.append(curr_node.left)
                        visited_node.add(curr_node.left)

                    if curr_node.right and curr_node.right not in visited_node:
                        q.append(curr_node.right)
                        visited_node.add(curr_node.right)
                    
                    if curr_node in parent_hash and parent_hash[curr_node] not in visited_node:
                        q.append(parent_hash[curr_node])
                        visited_node.add(parent_hash[curr_node])



                curr_level += 1

                

            result = []

            while q:
                result.append(q.popleft().val)

            return result 

        return find_distance(target,k)
        
