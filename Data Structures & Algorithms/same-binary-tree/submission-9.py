# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ar1 = []
        ar2 = []
        def dfs(root, ar): 
            if not root:
                ar.append(-1)
                return True
            ar.append(root.val)
            dfs(root.left, ar)
            dfs(root.right, ar)
        dfs(p, ar1)
        dfs(q, ar2)
        print(ar1)
        print(ar2)
        return ar1 == ar2