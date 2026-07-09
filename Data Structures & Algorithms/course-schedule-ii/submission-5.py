class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pmap = defaultdict(list)
        indegree = [0] * numCourses
        for cr, pre in prerequisites:
            pmap[pre].append(cr)
            indegree[cr]+=1
        order = []
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                order.append(i)
                q.append(i)
        
        while q:
            sz = len(q)
            for i in range(sz):
                crs = q.popleft()
                for j in pmap[crs]:
                    indegree[j]-=1
                    if indegree[j]==0:
                        q.append(j)
                        order.append(j)
                pmap[crs] = []
        if len(order)!=numCourses:
            return []
        return order
        