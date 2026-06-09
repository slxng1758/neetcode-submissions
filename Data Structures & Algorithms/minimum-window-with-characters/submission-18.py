class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(t)>len(s)):
            return ""
        fmap1 = dict(Counter(t))
        fmap2 = defaultdict(int)
        res = s+" "
        l = 0
        for r in range(len(s)):
            fmap2[s[r]] +=1
            while (all(fmap2[c] >= fmap1[c] for c in fmap1)):
                fmap2[s[l]] -=1
                if (fmap2[s[l]]==0):
                    del fmap2[s[l]]
                l+=1
                if (len(s[l-1:r+1])<len(res)):
                    res = s[l-1:r+1]
        if (res == s+" "):
            return ""
        return res
        