# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        s1 = [root]
        s2 =[]
        postorder=[]
        if root is None:
            return postorder
        while(s1):
            root = s1.pop()
            s2.append(root.val)
            if root.left:
                s1.append(root.left)
            if root.right:
                s1.append(root.right)
        # while(s2):
        #     r = s2.pop()
        #     postorder.append(r.val)
        return s2[::-1]
        