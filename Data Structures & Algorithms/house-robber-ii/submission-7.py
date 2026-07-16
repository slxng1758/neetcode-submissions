class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        
        r1 = [0]*len(nums)
        r2 = [0]*len(nums)
        r1[0] = nums[0]
        r1[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)-1):
            r1[i] = max(r1[i-1], nums[i]+r1[i-2])

        if len(nums)<3:
            return r1[1]
        
        r2[1] = nums[1]
        r2[2] = max(nums[1],nums[2])
        for i in range(3, len(nums)):
            r2[i] = max(r2[i-1], nums[i]+r2[i-2])

        return max(r1[len(nums)-2], r2[len(nums)-1])
        