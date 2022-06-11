class Solution: 
    def climbStairs(self, n: int) -> int:
        C = {1:1,2:2}
        def cs(num):
            if num in C:
                return C[num]
            else:
                C[num]=cs(num-1)+cs(num-2)
                return C[num]
        return(cs(n))    
        