class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = [False] *n
        d1 = [False] * n*2
        d2 = [False] *n*2
        board = [["."] * n for i in range(n)]
        def dfs(i):
            if i == n:
                cop = ["".join(row) for row in board]
                res.append(cop)
                return
            for c in range(n):
                if col[c] or d1[i+c] or d2[i-c+n]:
                    continue
                col[c] = True
                d1[i+c] = True
                d2[i-c+n] = True
                board[i][c] = "Q"
                dfs(i+1)
                board[i][c] = "."
                col[c] = False
                d1[i+c] = False
                d2[i-c+n] = False
        dfs(0)
        return res
        