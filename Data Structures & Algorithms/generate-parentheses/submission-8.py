class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subs = []
        def backtrack(i,j):
            nonlocal subs
            if (len(subs)==2*n):
                res.append("".join(subs))
                return
            if (i>j and j<n):
                subs.append(")")
                backtrack(i, j+1)
                subs.pop()
            if (i<n):
                subs.append("(")
                backtrack(i+1,j)
                subs.pop()
        backtrack(0,0)
        return res
        