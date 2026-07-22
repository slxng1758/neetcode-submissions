class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, cbuy):
            if i>=len(prices):
                return 0
            skip = dfs(i+1, cbuy)
            if (i,cbuy) in dp:
                return dp[(i,cbuy)]
            if cbuy:
                buy = dfs(i+1, False) - prices[i]
                dp[(i,True)] = max(buy, skip)

            if not cbuy:
                sell = dfs(i+2, True) + prices[i]
                dp[(i, False)] = max(sell, skip)
            return dp[(i, cbuy)]
            
        return dfs(0,True)
        