import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Check if the input list of linked lists is empty or None
        if not lists:
            return None 

        # Initialize a min-heap to keep track of the smallest element from each linked list
        min_heap = []

        # Populate the heap with the first element from each non-empty linked list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        # Initialize a dummy node to build the result linked list
        dummy = ListNode()
        curr = dummy

        # Process the min-heap until it is empty
        while min_heap:
            # Pop the smallest element from the heap
            val, index, node = heapq.heappop(min_heap)

            # Add the popped element to the result linked list
            curr.next = ListNode(val)
            curr = curr.next 

            # Move to the next element in the corresponding list
            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))

        # Return the merged sorted linked list
        return dummy.next
