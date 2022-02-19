# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def Maxi(root):  
            if (root == None):
                return 0
            else:
                left = Maxi(root.left)
                right = Maxi(root.right)
                return max(left,right)+1
        return(Maxi(root))