class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        nums[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            nums[i]= max(nums[i-1],nums[i-2]+nums[i])
        return nums[-1]