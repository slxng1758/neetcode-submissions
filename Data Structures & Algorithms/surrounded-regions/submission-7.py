class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ar = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!='O' or ar[i][j]==1:
                return
            ar[i][j] = 1
            for x,y in dir:
                dfs(i+x,j+y)

        for i in range(len(board)):
            if i==0 or i == len(board)-1:
                for j in range(len(board[0])):
                    if board[i][j]=='O':
                        dfs(i,j)
            else:
                if board[i][0]=='O':
                    dfs(i,0)
                if board[i][len(board[0])-1]=='O':
                    dfs(i,len(board[0])-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if ar[i][j]!=1:
                    board[i][j]='X'
        