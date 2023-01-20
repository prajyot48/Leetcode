#User function Template for python3


class Solution:
    # from collections import deque
    
    from collections import deque 
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        
        indegree = [0]*V
        for arr in adj:
            for i in arr:
                indegree[i] = indegree[i]+1
        queue = []
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        cnt = 0
        # top_order = []
        while queue:
            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            # top_order.append(u)
            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in adj[u]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            cnt += 1
            
        if cnt == V:
            return 0
            
        
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends