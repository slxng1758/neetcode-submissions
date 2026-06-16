# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        q = deque()
        if root:
            q.append(root)
        while q:
            qsize = len(q)
            for i in range(qsize):
                cur = q.popleft()
                if cur and cur.left:
                    q.append(cur.left)
                if cur and cur.right:
                    q.append(cur.right)
            depth+=1
        return depth


        