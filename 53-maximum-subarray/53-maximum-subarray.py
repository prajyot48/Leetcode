class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # print(nums)
        sumVal = 0
        ret = 0
        for i in nums:
            sumVal = max(0, sumVal) + i
            # print("sumVal",sumVal,i)
            ret = max(ret, sumVal)
            # print("Ret",ret,"Sumval",sumVal)
        return max(nums) if ret == 0 else ret