class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subs = []
        def palindrome(st):
            return st == st[::-1]
        def dfs(i):
            if i == len(s):
                res.append(subs.copy())
                return
            for j in range(i,len(s)):
                if (palindrome(s[i:j+1])):
                    subs.append(s[i:j+1])
                    dfs(j+1)
                    subs.pop()
        dfs(0)
        return res
        