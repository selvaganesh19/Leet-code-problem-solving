# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def output(root,l,r):
            if not root:
                return True
            elif root.val >=r or root.val<=l:
                return False
            else:
                return output(root.left,l,root.val) and output(root.right, root.val, r)
        
        return output(root,float('-inf'),float('inf'))