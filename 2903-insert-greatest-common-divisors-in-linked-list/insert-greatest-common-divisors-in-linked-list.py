# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b > 0:
                a, b = b, a%b
            return a
        
        curr = head 

        while curr.next:
            new_num = gcd(curr.val, curr.next.val)
            new_node = ListNode(new_num)
            tmp = curr.next 
            curr.next = new_node
            new_node.next = tmp 
            curr = tmp

        return head
