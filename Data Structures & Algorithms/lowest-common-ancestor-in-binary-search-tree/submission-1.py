# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def in_tree(self, tree, value):
        if not tree:
            return False
        return (tree.val == value) or (self.in_tree(tree.left, value)) or self.in_tree(tree.right, value)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root.val == p.val or root.val == q.val:
            return TreeNode(root.val)

        p_in_left = self.in_tree(root.left, p.val)
        q_in_left = self.in_tree(root.left, q.val)
        p_in_right = self.in_tree(root.right, p.val)
        q_in_right = self.in_tree(root.right, q.val)

        if (p_in_right and q_in_left) or (q_in_right and p_in_left):
            return TreeNode(root.val)
        
        if (p_in_right) and q_in_right:
            return self.lowestCommonAncestor(root.right, p, q)

        if p_in_left and q_in_left:
            return self.lowestCommonAncestor(root.left, p, q)

        
        
