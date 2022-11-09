class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        z=0
        mul = 1
        for i in nums:
            mul*=i
            if i==0:
                z+=1
                continue
            prod *= i
        if z>1:
            return [0]*len(nums)
        res=[]
        for i in nums:
            if i == 0:
                res.append(prod)
            else:
                res.append(mul//i)
        return res
        
        