class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<4:
            return max(nums)
        def Helper(arr):
            arr.append(0)
            arr[1]=max(arr[0],arr[1])
            for i in range(2,len(arr)):
                arr[i] = max(arr[i]+arr[i-2],arr[i-1])
            return arr[-1]
        return max(Helper(nums[:-1]),Helper(nums[1:]))
                
        