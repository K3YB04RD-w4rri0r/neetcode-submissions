# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)

        merged = []
        for l, r in zip_longest(left, right, fillvalue=[]):
            merged.append(l + r)

        return [[root.val]] + merged
