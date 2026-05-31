class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += str(len(strs[i]))+"#"+strs[i]
        return s

    def decode(self, s: str) -> List[str]:
        lis = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            lis.append(s[i:j])
            i = j
        return lis


