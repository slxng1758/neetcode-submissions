class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if (len(edges)!=n-1):
            return False 

        tree = True
        vis = set()
        pmap = defaultdict(list)

        for a,b in edges:
            pmap[a].append(b)
            pmap[b].append(a)

        def dfs(i, par):
            nonlocal tree
            if i in vis:
                tree = False
                return
            vis.add(i)
            for j in pmap[i]:
                if j ==par:
                    continue
                dfs(j, i)
            return

        dfs(0,-1)
        return tree and len(vis) == n

        