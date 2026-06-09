class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ct = 0
        fmap = defaultdict(int)
        maxf = 0
        l = 0
        for r, let in enumerate(s):
            fmap[let] = fmap[let]+1
            maxf = max(maxf, fmap[let])
            if (r-l+1-maxf>k):
                fmap[s[l]] = fmap[s[l]]-1
                l+=1
            ct = max(ct, r-l+1)
        return ct
        