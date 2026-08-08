# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hd = ListNode()
        curr = hd
        heap = []
        heapq.heapify(heap)
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i))

        while heap:
            cur, idx = heapq.heappop(heap)
            curr.next = lists[idx]
            curr = curr.next
            lists[idx] = lists[idx].next
            nw = lists[idx]
            if nw:
                heapq.heappush(heap, (nw.val, idx))
        return hd.next
            
        