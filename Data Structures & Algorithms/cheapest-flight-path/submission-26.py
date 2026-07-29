class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        fmap = defaultdict(list)
        dist = [float("inf")]*n
        for i in range(len(flights)):
            ff, ft, price = flights[i]
            fmap[ff].append((ft,price))
        q = deque([(src, 0, 0)])
        dist[src] = 0
        for i in range(k+1):
            qsize = len(q)
            for j in range(qsize):
                cur, cos, stops = q.popleft()
                if stops>k:
                    continue
                for nei in fmap[cur]:
                    port, price = nei
                    if cos+price<dist[port]:
                        dist[port] = min(cos+price, dist[port])
                        q.append((port, cos+price, stops+1))
        return dist[dst] if dist[dst]!=float("inf") else -1