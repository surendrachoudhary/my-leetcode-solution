# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize slow and fast pointers to the head of the linked list
        slow, fast = head, head

        # Move slow pointer by one step and fast pointer by two steps
        # to detect the presence of a cycle in the linked list
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

            # If slow and fast pointers meet, it indicates the presence of a cycle
            if slow == fast:
                # Reset fast pointer to the head of the linked list
                fast = head

                # Move both pointers at the same pace until they meet again
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                
                # Return the node where both pointers meet, which is the start of the cycle
                return slow
        
        # If the loop exits without finding a cycle, print "No cycle"
        print("No cycle")
