# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        

        # Initialize slow and fast pointers
        slow, fast = head, head

        # Move slow pointer by one step and fast pointer by two steps
        # to find the midpoint of the linked list
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next

        # Store the head of the second half of the linked list
        next_head = slow.next
        # Disconnect the first half from the second half
        slow.next = None

        # Reverse the second half of the linked list
        prev, curr, after = None, next_head, next_head.next if next_head else None
        while curr:
            curr.next = prev
            prev = curr
            curr = after
            after = after.next if after else None 
        
        # Compare values of the first half with the reversed second half
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True
