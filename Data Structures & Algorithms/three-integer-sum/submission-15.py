class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        id = 0
        ls = []
        while id<len(nums)-2:
            while id>0 and id<len(nums)-1 and nums[id]==nums[id-1]:
                id+=1
            tg = -1*nums[id]
            l = id+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r]==tg:
                    ls.append([nums[id],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                if nums[l]+nums[r]<tg:
                    l+=1
                if nums[l]+nums[r]>tg: 
                    r -=1
            id+=1
        return ls
        