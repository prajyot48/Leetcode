class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s,l,ls):
            if s > l:
                return 
            ls[s],ls[l] = ls[l],ls[s]
            helper(s+1,l-1,ls)
        helper(0,len(s)-1,s)
        