# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a dummy node to simplify handling the first group
        dummy = ListNode(0, head)
        # Initialize groupPrev to the dummy node
        groupPrev = dummy

        # Loop until there are no more groups of size k
        while True:
            # Get the kth node in the current group
            kth = self.getKth(groupPrev, k)

            # If there are fewer than k nodes left, break the loop
            if not kth:
                break
            
            # Save the next node after the current group
            groupNext = kth.next 

            # Reverse the current group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            # Connect the reversed group to the previous group
            tmp = groupPrev.next 
            groupPrev.next = kth 
            groupPrev = tmp 

        # Return the modified linked list
        return dummy.next

    # Helper function to get the kth node from the current position
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
