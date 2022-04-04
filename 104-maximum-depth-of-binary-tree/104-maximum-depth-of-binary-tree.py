# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        hl=  1+ self.maxDepth(root.left)
        hr = 1 + self.maxDepth(root.right)
        return max(hl,hr)
        # return 1+max(hl,hr)
        
        #//using bfs
        # res = []
        # q=deque([root])
        # # q.append(root)
        # level=0
        # while q:
        #     qlen = len(q)
        #     level=[]
        #     for i in range(qlen):
        #         node = q.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     if level:
        #         res.append(level)
        #     print(res)
        # return(level)
        
        
        # def Maxi(root):  
        #     if (root == None):
        #         return 0
        #     else:
        #         left = Maxi(root.left)
        #         # print("LEFT",root.val,left)
        #         right = Maxi(root.right)
        #         # print("RIGHT",root.val,right)
        #         return max(left,right)+1
        # return(Maxi(root))