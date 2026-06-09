class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        prof = 0
        for i in range(len(prices)):
            buy = min(buy,prices[i])
            prof = max(prices[i]-buy,prof)
        return prof
            


        