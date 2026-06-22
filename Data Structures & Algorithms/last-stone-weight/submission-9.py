class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        print(maxHeap)
        while (len(maxHeap)>1):
            first = heapq.heappop(maxHeap)
            sec = heapq.heappop(maxHeap)
            if first != sec:
                heapq.heappush(maxHeap,first-sec)
        if maxHeap:
            return abs(heapq.heappop(maxHeap))
        return 0

        