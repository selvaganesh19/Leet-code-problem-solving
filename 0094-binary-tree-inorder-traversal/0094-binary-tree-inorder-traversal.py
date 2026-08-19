# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res , st = [],[]
        node = root


        while st or node:
            while node:
                st.append(node)
                node = node.left
            
            node = st.pop()
            res.append(node.val)

            node = node.right
        
        return res

