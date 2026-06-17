# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cdiam = self.maxheight(root.right) + self.maxheight(root.left)
        nextdiam = max(self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))

        return max(cdiam,nextdiam)

    def maxheight(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0
        return 1+max(self.maxheight(root.right), self.maxheight(root.left))
        