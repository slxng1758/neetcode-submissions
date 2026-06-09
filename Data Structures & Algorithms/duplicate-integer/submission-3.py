class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                return True
        return False
        