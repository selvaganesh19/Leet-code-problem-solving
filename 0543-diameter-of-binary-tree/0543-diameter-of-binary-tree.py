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

        if not root: return 0

        st , height,ans , res = [(root,False)] , defaultdict(int), 0,0

        while st:
            node , seen = st.pop()

            if not node: continue

            if not seen:
                st.append((node,True))
                st.append((node.left,False))
                st.append((node.right,False))
            else:
                l , r = height[node.left],height[node.right]
                res = max(res,l+r)
                height[node] = 1 + max(l, r)
            
        
        return res

