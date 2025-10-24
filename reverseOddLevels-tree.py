# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(leftchild,rightchild,level):
            if not leftchild or not rightchild:
                return
            if level % 2 == 0:
                leftchild.val, rightchild.val = rightchild.val, leftchild.val
            dfs(leftchild.left, rightchild.right, level+1)
            dfs(leftchild.right, rightchild.left, level+1)
        
        dfs(root.left, root.right, 0)
        return root
        