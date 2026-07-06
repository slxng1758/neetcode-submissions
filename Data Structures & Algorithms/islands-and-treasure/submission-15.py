class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dx = [1,0,0,-1]
        dy = [0,1,-1,0]
        INF = 2147483647
        ts = []
        def bfs(ls):
            q = deque(ts)
            steps = 0
            while q:
                sz = len(q)
                for i in range(sz):
                    r, c = q.popleft()
                    if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]) and (grid[r][c]==0 or grid[r][c]==INF):
                        if grid[r][c] == INF:
                            grid[r][c] = steps
                        for j in range(4):
                            q.append((r+dx[j],c+dy[j]))
                steps +=1
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    ts.append((i,j))
        
        bfs(ts)
        