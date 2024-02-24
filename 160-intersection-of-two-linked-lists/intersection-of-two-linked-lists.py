# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d1 = headA
        d2 = headB
        
        # Traverse until both pointers reach the end of their respective linked lists
        while d1 != d2:
            # Move d1 to the next node in list A or to the head of list B if it reaches the end
            d1 = headB if d1 is None else d1.next
            # Move d2 to the next node in list B or to the head of list A if it reaches the end
            d2 = headA if d2 is None else d2.next
            
        # If both pointers become None, there is no intersection
        # If they point to the same node, it is the intersection node
        return d1
