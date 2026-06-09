class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1)>len(s2)):
            return False

        fmap1 = dict(Counter(s1))
        fmap2 = defaultdict(int)
        wsize = len(s1)
        for i in range(wsize):
            fmap2[s2[i]] = fmap2[s2[i]]+ 1
        for i in range(len(s2)-wsize):
            print(fmap1,fmap2)
            if (fmap1==fmap2):
                return True
            fmap2[s2[i]] -= 1
            if fmap2[s2[i]] == 0:
                del fmap2[s2[i]]
            fmap2[s2[i+wsize]] +=1
        return fmap1==fmap2


        