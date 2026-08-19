# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        res, st = [], [root] if root else []

        while st:
            node = st.pop()
            node.left, node.right = node.right, node.left
            
            if node.left:
                st.append(node.left)

            if node.right:
                st.append(node.right)
        
        return root