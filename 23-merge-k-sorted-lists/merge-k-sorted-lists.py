# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        def merge2list(list1, list2):
            cur = dummy = ListNode()
            while list1 and list2:               
                if list1.val < list2.val:
                    cur.next = list1
                    list1, cur = list1.next, list1
                else:
                    cur.next = list2
                    list2, cur = list2.next, list2
                    
            if list1 or list2:
                cur.next = list1 if list1 else list2
                
            return dummy.next


        head = lists[0]
        for i in lists[1:]:
            if i:
              head = merge2list(head, i)
            else:
                continue

        return head

        