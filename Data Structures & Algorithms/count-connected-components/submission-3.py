class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comps = 0
        pmap = defaultdict(list)
        vis = set()

        for a,b in edges:
            pmap[a].append(b)
            pmap[b].append(a)

        def dfs(i):
            if i in vis:
                return 
            vis.add(i)
            for j in pmap[i]:
                if j==i:
                    continue
                dfs(j)
            return

        for i in range(n):
            if i not in vis:
                comps+=1
                dfs(i)
        
        return comps