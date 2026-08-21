# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        idx = {v: i for i,v in enumerate(inorder)}

        ps = len(postorder)-1

        def build(l,r):
            nonlocal ps
            
            if l>= r:
                return None
            
            root = TreeNode(postorder[ps])
            ps-=1
            mid = idx[root.val]
            root.right = build(mid+1,r)
            root.left = build(l,mid)
            return root
        
        return build(0, len(inorder))