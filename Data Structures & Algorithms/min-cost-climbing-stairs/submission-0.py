class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mcost = [float("inf")]*len(cost)
        mcost[0] = cost[0]
        mcost[1]= cost[1]
        for i in range(2,len(cost)):
            mcost[i] = cost[i] + min(mcost[i-1],mcost[i-2])
        return min(mcost[n-1], mcost[n-2])

        