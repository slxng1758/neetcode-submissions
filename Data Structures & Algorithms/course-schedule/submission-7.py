class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        vis = set()
        cycle = True

        for i in range(len(prerequisites)):
            first = prerequisites[i][0]
            sec = prerequisites[i][1]
            graph[first].append(sec)
        print(graph)
        
        def dfs(i):
            nonlocal cycle
            if i in vis:
                cycle = False
                return 
            vis.add(i)
            for j in graph[i]:
                dfs(j)
            vis.remove(i)
            graph[i] = []
            return

        for i in range(numCourses):
            if i not in vis:
                dfs(i)
        return cycle

