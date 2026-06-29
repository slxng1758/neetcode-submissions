class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subs = "("
        def backtrack(i,j):
            nonlocal subs
            if (len(subs)==2*n):
                res.append(subs)
                return
            if (i>j and j<n):
                subs += ")"
                backtrack(i, j+1)
                subs = subs[:-1]
            if (i<n):
                subs +="("
                backtrack(i+1,j)
                subs = subs[:-1]
        backtrack(1,0)
        return res
        