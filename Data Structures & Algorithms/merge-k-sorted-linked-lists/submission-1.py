# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            heapq.heappush(heap, (node.val, i, node))
        start = ListNode()
        cur = start
        while heap:
            val, i, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            cur.next = node
            cur = cur.next
        return start.next