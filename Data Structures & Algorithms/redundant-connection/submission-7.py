class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edge = []
        vis = set()
        cset = set()
        cstart = -1
        pmap = defaultdict(list)

        for a,b in edges:
            pmap[a].append(b)
            pmap[b].append(a)

        def dfs(i, par):
            nonlocal cstart
            if i in vis:
                cstart = i
                return True
            vis.add(i)
            for j in pmap[i]:
                if j==par:
                    continue
                if dfs(j,i):
                    if cstart !=-1:
                        cset.add(i)
                    if i==cstart:
                        cstart = -1
                    return True
            return False

        dfs(1, 0)
        for u,v in reversed(edges):
            if u in cset and v in cset:
                return [u,v]
        return []