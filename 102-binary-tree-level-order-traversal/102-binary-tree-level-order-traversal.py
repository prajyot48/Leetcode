# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=deque([root])
        while q:
                qlen = len(q)
                lev=[]
                for i in range(qlen):
                    node = q.popleft()
                    if node:
                        lev.append(node.val)
                    # if node.left:
                        q.append(node.left)
                    # if node.left:
                        q.append(node.right)
                if lev:
                    res.append(lev)
        return res