# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Convert the given linked list into a number
        number = 0
        while head:
            number = number * 10 + head.val
            head = head.next

        # Double the number
        doubled_number = number * 2

        # Convert the doubled number back to a linked list
        if doubled_number == 0:
            return ListNode(0)  # Handle the case when the doubled number is 0
        else:
            result_head = None
            while doubled_number:
                digit = doubled_number % 10
                doubled_number //= 10
                result_head = ListNode(digit, result_head)
            return result_head

