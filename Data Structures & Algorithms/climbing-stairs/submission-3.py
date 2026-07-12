class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        dp.append(1)
        dp.append(2)
        i = 2
        while i<=n:
            dp.append(dp[i-1]+dp[i-2])
            i+=1
        return dp[n-1]
        