class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        marea = 0
        dx = [1,0,0,-1]
        dy = [0,1,-1,0]

        def dfs(i,j):
            nonlocal marea
            if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0):
                return 0
            grid[i][j]=0
            area = 1
            for k in range(4):
                area += dfs(i+dx[k],j+dy[k])
            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    marea = max(marea, dfs(i,j))
        return marea
        