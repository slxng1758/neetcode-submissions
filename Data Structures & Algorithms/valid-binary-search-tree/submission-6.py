# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        low = -1001
        high = 1001
        def dfs(root, low, high):
            nonlocal valid
            if not root:
                return True
            if not (root.val > low and root.val < high):
                valid = False
                return False
            dfs(root.left, low, root.val)
            dfs(root.right, root.val, high)
        dfs(root, low, high)
        return valid
        