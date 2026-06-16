# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self, root, interval):
        if not root:
            return True
        return ((interval[0] < root.val < interval[1])
               and self.isValid(root.left, [interval[0],root.val])
               and self.isValid(root.right, [root.val, interval[1]]))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isValid(root, [float("-inf"), float("+inf")])


        
        