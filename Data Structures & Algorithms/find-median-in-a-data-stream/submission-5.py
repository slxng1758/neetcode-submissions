class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def addNum(self, num: int) -> None:
        mhigh, mlow = 0,0
        if self.minHeap:
            mhigh = self.minHeap[0]
        if self.maxHeap:
            mlow = -self.maxHeap[0]
        if num >=mhigh:
            heapq.heappush(self.minHeap,num)
        else:
            heapq.heappush(self.maxHeap, -num)

        while len(self.minHeap)-len(self.maxHeap)>1:
            switch = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -switch)
        while len(self.maxHeap)-len(self.minHeap)>1:
            switch = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -switch)
        

    def findMedian(self) -> float:
        if len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap)>len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (self.minHeap[0]-self.maxHeap[0])/2
        
        