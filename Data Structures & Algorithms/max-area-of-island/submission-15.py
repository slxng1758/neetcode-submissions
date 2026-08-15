class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mar = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(x, y):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]):
                return 0
            if grid[x][y]!=1:
                return 0
            grid[x][y]=0
            area = 1
            for dx, dy in dirs:
                area += dfs(x+dx, y+dy)
            return area
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    mar = max(mar, dfs(i,j))

        return mar

        