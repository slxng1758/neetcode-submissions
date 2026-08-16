"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lcopy = defaultdict(lambda: Node(0))
        lcopy[None] = None

        cur = head
        while cur:
            lcopy[cur].val = cur.val
            lcopy[cur].next = lcopy[cur.next]
            lcopy[cur].random = lcopy[cur.random]
            cur = cur.next
        return lcopy[head]