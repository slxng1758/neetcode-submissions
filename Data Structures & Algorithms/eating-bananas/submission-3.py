class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l<=r:
            mid = l +((r-l)//2)
            k = self.sim(mid, piles)
            if k<=h:
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res
            
                
    def sim(self, i: int, piles: List[int]) -> int:
        hrs = 0
        for b in piles:
            hrs += math.ceil(b/i)
        return hrs


        