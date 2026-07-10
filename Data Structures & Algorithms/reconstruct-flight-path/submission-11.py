class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        fmap = defaultdict(list)
        for u,v in tickets:
            fmap[u].append(v)

        for i in fmap:
            fmap[i].sort(reverse=True)

        vis = set()
        path = []
        subs = ["JFK"]

        def dfs(node):
            while fmap[node]:
                nx = fmap[node].pop()
                dfs(nx)
            path.append(node)

        dfs("JFK")
        return path[::-1]
        