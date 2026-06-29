class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subs = []
        nums.sort()
        def dfs(i):

            res.append(subs.copy())

            for j in range(i, len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                subs.append(nums[j])
                dfs(j+1)
                subs.pop()
        dfs(0)
        return res