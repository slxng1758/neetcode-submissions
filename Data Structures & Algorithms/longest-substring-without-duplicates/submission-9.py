class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s)<2):
            return len(s)
        hset = set()
        l, r = 0,1
        lsub = 1
        hset.add(s[l])
        while (l<=r and r<len(s)):
            if s[r] not in hset:
                hset.add(s[r])
                r+=1
            else:
                hset.remove(s[l])
                l+=1
            print(l,r)
            lsub = max(lsub, r-l)
        return lsub


        