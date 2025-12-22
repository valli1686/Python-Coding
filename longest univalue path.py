# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        self.max = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            la = ra = 0
            if node.left and node.left.val == node.val:
                la = left
            if node.right and node.right.val == node.val:
                ra = right
            self.max = max(self.max , la + ra + 1)
            return max(la,ra) + 1
        dfs(root)
        return self.max - 1 if self.max > 0 else 0
        