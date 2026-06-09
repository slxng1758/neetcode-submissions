class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        mlen = 0
        for i in nums:
            if i-1 not in nset:
                len = 0
                while i in nset:
                    len += 1
                    i += 1
                mlen = max(len,mlen)
        return mlen

        