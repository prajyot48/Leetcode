# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def HeightheckC(self,root):
            if root is None:
                return 0
            nl =  self.HeightheckC(root.left)
            if nl == -1:
                return -1
            nr = self.HeightheckC(root.right)
            if nr == -1:
                return -1
            if abs(nr - nl)>1:
                return -1
            return 1+max(nr,nl)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.HeightheckC(root) != -1
        