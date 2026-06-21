# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        llist = []
        q = []
        if root:
            q.append(root)
        while q:
            subl = []
            lsize = len(q)
            for i in range(lsize):
                node = q.pop(0)
                if node:
                    subl.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            llist.append(subl)
        return llist
                