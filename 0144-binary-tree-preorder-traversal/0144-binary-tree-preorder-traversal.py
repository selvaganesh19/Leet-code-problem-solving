# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        res , st = [] , [root] if root else []

        while st:
            node = st.pop()
            res.append(node.val)

            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        
        return res