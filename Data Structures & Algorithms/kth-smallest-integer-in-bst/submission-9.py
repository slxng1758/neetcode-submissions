# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ar = []
        def dfs(root):
            nonlocal ar
            if not root:
                return True
            
            dfs(root.left)
            ar.append(root)
            dfs(root.right)

        dfs(root)
        return ar[k-1].val
        