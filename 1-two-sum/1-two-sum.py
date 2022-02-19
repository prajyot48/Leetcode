class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}
        for i in range(0,len(nums)):
            dif = target - nums[i]
            if dif in lookup:
                return [lookup[dif],i]
            lookup[nums[i]]=i
        return None