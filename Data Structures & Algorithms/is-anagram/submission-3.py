class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}
        for i in range(len(s)):
            if s[i] not in ms:
                ms[s[i]] = 1
            else:
                ms[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in mt:
                mt[t[i]] = 1
            else:
                mt[t[i]]+=1
        return ms == mt
        