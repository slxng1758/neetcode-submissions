"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj = defaultdict(list)
        if node==None:
            return None
        start = node
        q = deque([node])
        adj[node] = Node(node.val)
        while q:
            cur = q.popleft()
            for i in cur.neighbors:
                if i not in adj:
                    adj[i] = Node(i.val)
                    q.append(i)
                adj[cur].neighbors.append(adj[i])
        return adj[node]