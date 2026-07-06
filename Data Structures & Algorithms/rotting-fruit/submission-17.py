class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx = [1,0,0,-1]
        dy = [0,1,-1,0]
        rot = []
        health = 0
        steps = 0
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    rot.append((i,j))
                if grid[i][j]==1:
                    health +=1
        q = deque(rot)
        while q and health>0:
            sz = len(q)
            for i in range(sz):
                r,c = q.popleft()
                for k in range(4):
                    if not (r+dx[k]<0 or c+dy[k]<0 or r+dx[k]>=len(grid) or c+dy[k]>=len(grid[0]) or grid[r+dx[k]][c+dy[k]]!=1):
                        q.append((r+dx[k],c+dy[k]))
                        grid[r+dx[k]][c+dy[k]]=2
                        health -= 1
            steps+=1

        if health!=0:
            return -1
        return steps
