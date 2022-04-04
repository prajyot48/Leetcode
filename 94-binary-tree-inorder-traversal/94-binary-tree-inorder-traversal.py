# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
class Solution:
    # @param root, a tree node
    # @return a list of integers
    # res = []
    # def iot(self, root):
    #     if root == None:
    #         return
    #     else:
    #         self.iot(root.left)
    #         self.res.append(root.val)
    #         self.iot(root.right)
            
    def inorderTraversal(self, root):
        current = root
        stack = [] # initialize stack
        inorder = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                inorder.append(current.val)
                # print(current.val, end=" ") # Python 3 printing
                current = current.right
            else:
                break
        return inorder