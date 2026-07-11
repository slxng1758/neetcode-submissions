class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        vis = set()
        def sim(i,j,t):
            if min(i,j)<0 or max(i,j)>=len(grid) or (i,j) in vis or grid[i][j]>t:
                return False
            if i==j and j == len(grid)-1:
                return True
            vis.add((i,j))
            return sim(i+1,j,t) or sim(i-1,j,t) or sim(i,j+1,t) or sim(i,j-1,t)
            vis.remove((i,j))
            return False

        minh, maxh = grid[0][0], grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid)):
                minh = min(minh, grid[i][j])
                maxh = max(maxh, grid[i][j])
        
        while minh<maxh:
            mid = minh+(maxh-minh)//2
            if sim(0,0,mid):
                maxh = mid
            else:
                minh = mid+1
            vis.clear()

        return minh

        


        