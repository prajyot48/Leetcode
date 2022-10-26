class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [1 for _ in range(n)]
        for i in range(2,n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]+dp[-2]
        
        