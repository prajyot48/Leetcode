class Solution:
    def rob(self, nums: List[int]) -> int:
        def Helper(nums):
            n = len(nums)
            if n <3:
                return max(nums)
            s = [0] * (n)
            s[0]=nums[0]
            s[1]=max(nums[0],nums[1])
            for i in range(2,n):
                s[i] = max(s[i-2]+nums[i],s[i-1])
            return max(s[-2],s[-1])
        if len(nums) <3:
                return max(nums)
        return max(Helper(nums[1:]),Helper(nums[:-1]))
        