class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        nums=sorted(set(nums))
        n = len(nums)
        s = [0] * n
        # s[0] = nums[0]*c[nums[0]]
        earn1,earn2 =0,0
        for i in range(n):
            cur = nums[i]*c[nums[i]]
            if i > 0 and nums[i] == nums[i-1]+1:
                temp = earn2
                earn2 = max(cur+earn1,earn2)
                earn1=temp
            else:
                temp = earn2
                earn2 = cur+earn2
                earn1=temp
                
        return earn2
                
                