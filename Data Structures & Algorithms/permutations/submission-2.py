class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i):
            if i==len(nums)-1:
                res.append(nums.copy())
            for idx in range(i, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                dfs(i+1)
                nums[i], nums[idx] = nums[idx], nums[i]
        dfs(0)
        return res
        