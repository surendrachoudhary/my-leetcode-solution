# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate the length of linked list A
        countA = 0
        tmp = headA
        while tmp:
            countA += 1
            tmp = tmp.next

        # Calculate the length of linked list B
        countB = 0
        tmp = headB
        while tmp:
            countB += 1
            tmp = tmp.next 

        # Move pointers to the same starting position
        tmp1, tmp2 = headA, headB
        if countA > countB:
            step = countA - countB
            for i in range(step):
                tmp1 = tmp1.next
        elif countA < countB:
            step = countB - countA
            for i in range(step):
                tmp2 = tmp2.next 

        # Move both pointers until they meet
        while tmp1 != tmp2:
            tmp1 = tmp1.next 
            tmp2 = tmp2.next
        
        # Return the intersection node or None if no intersection
        return tmp1
