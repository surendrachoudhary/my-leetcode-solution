# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Create a set to store nodes from list A
        seen_nodes = set()

        # Traverse list A and store nodes in the set
        tmp = headA
        while tmp:
            seen_nodes.add(tmp)
            tmp = tmp.next

        # Traverse list B and check if any node is in the set
        tmp = headB
        while tmp:
            if tmp in seen_nodes:
                return tmp  # Return the node
            tmp = tmp.next

        return None  # Return None if no intersection node found
