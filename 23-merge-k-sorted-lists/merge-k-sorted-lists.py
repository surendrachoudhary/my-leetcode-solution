# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node_array = []
        for i in lists:
            if i:
                while i:
                    node_array.append(i.val)
                    i = i.next 
            else:
                continue
        
        dummy = ListNode(0)
        tmp = dummy

        node_array.sort()

        for node in node_array:
            tmp.next = ListNode(node)
            tmp = tmp.next

        return dummy.next
