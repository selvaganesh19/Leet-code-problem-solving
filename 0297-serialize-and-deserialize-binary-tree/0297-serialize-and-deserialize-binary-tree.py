# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        out = []

        def dfs(root):
            if not root:
                out.append("#")
                return
            
            out.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ','.join(out)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split(","))
        
        def build():
            v = next(vals)
            if v == "#":
                return None
            

            root = TreeNode(int(v))
            root.left = build()
            root.right = build()
            
            return root
        
        return build()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))