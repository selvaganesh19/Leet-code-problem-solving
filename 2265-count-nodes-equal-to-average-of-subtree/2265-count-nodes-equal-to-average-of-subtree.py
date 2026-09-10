# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0,0
            
            leftheight,leftsum = dfs(root.left)
            rightheight,rightsum = dfs(root.right)

            sum = leftsum + rightsum + root.val

            height = leftheight + rightheight + 1

            if sum // height == root.val:
                self.res+=1
            
            return height,sum
            
        dfs(root)
        return self.res