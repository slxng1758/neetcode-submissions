class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        dirs = [[-1,0], [1,0],[0,1],[0,-1]]
        def dfs(x,y):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]): 
                return
            if grid[x][y]!="1":
                return
            grid[x][y] = "0"
            for dx, dy in dirs:
                dfs(x+dx, y+dy)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i,j)
                    cnt+=1

        return cnt