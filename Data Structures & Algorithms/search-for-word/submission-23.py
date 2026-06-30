class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j, idx): #u,l,r,d 
            if idx == len(word):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[idx]:
                return False
            board[i][j]= "."
            res = (backtrack(i,j+1,idx+1) or
                    backtrack(i,j-1, idx+1) or
                    backtrack(i-1,j, idx+1) or
                    backtrack(i+1,j, idx+1))
            board[i][j] = word[idx]
            return res


        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False


        