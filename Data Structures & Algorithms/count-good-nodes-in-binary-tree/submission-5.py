# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        cmax = root.val
        def dfs(root, cmax):
            nonlocal res
            if not root:
                return True
            if root.val >= cmax:
                res += 1
            cmax = max(cmax, root.val)
            dfs(root.left, cmax)
            dfs(root.right,cmax)
        dfs(root, cmax)
        return res
        