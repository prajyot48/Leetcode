# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans =[]
        q = q=deque([root])
        # q.append(root)
        while q :
            s = len(q)
            lev = []
            for i in range(s):
                node = q.popleft()
                # if node:
                if node:
                    lev.append(node.val)
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
                # level.append(node.val)
            if lev:
                ans.append(lev)
        return ans 
        # res=[]
        # q=deque([root])
        # while q:
        #     qlen = len(q)
        #     lev=[]
        #     for i in range(qlen):
        #         node = q.popleft()
        #         if node:
        #             lev.append(node.val)
        #         if node and node.left:
        #             q.append(node.left)
        #         if node and node.right:
        #             q.append(node.right)
        #     if lev:
        #         res.append(lev)
        # return res
           