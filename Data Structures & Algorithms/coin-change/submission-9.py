class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:
            return 0
        dp = [float('inf')]*(amount+1)
        dp[0]= 0
        for i in range(amount+1):
            for j in range(len(coins)):
                if i-coins[j]>=0:
                    dp[i]=min(dp[i],1+dp[i-coins[j]])
        print(dp)
        return -1 if dp[amount]==float('inf') else dp[amount]

        