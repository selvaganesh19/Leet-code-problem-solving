# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        res=[0]
        def dfs(n):
            if not n: return 0
            left,right=dfs(n.left),dfs(n.right)
            res[0]=max(res[0],left+right)
            return 1+max(left,right)
        dfs(root)
        return res[0]