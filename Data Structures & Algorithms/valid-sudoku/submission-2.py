class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        co = defaultdict(set)
        ro = defaultdict(set)
        sq = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] ==".":
                    continue
                if (board[r][c] in co[c]
                    or board[r][c] in ro[r]
                    or board[r][c] in sq[r//3,c//3]):
                    return False
                co[c].add(board[r][c])
                ro[r].add(board[r][c])
                sq[r//3,c//3].add(board[r][c])
        return True
        