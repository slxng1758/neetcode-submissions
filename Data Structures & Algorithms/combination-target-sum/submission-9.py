class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subs = []
        nums.sort()
        def dfs(i, csum):
            if (csum == target):
                res.append(subs.copy())
                return
            for j in range(i, len(nums)):
                if csum+nums[j]>target:
                    return
                subs.append(nums[j])
                dfs(j, csum+nums[j])
                subs.pop()
        dfs(0, 0)
        return res