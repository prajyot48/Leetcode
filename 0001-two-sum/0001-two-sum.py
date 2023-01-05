class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            val = nums[i]
            res =target - val
            if res in h:
                return [h[res],i]
            h[val]=i
        return [-1,-1]
        