# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root, p.val, q.val)
        
    def lca(self, root, n1, n2):
        if root:
            if root.val == n1 or root.val == n2:    
                return root
            left = self.lca(root.left, n1, n2)
            right = self.lca(root.right, n1, n2)
            if left and right:
                return root
            return left if left is not None else right