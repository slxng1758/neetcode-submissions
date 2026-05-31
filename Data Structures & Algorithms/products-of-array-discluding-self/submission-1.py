class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        psa = [1]
        for i in range(len(nums)-1):
            psa.append(psa[i]*nums[i])
        ssa = [1]*len(nums)
        ssa[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            ssa[i] = nums[i+1]*ssa[i+1]
        res = []
        for i in range(len(nums)):
            res.append(psa[i]*ssa[i])
        return res




        