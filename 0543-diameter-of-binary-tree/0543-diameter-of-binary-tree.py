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

        def depth(root,res):

            if not root: return 0

            left = depth(root.left,res)
            right = depth(root.right,res)

            res[0] = max(res[0],left+right)

            return max(left,right)+1
        
        res = [0]
        depth(root,res)

        return res[0]
