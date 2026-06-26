class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subs = []
        def dfs(i, csum):
            if (i>=len(nums) or csum>target):
                return
            if (csum == target):
                res.append(subs.copy())
                return
            subs.append(nums[i])
            dfs(i, csum+nums[i])
            subs.pop()
            dfs(i+1,csum)
        dfs(0, 0)
        return res