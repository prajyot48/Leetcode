class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while(i<j):
            sumi=numbers[i]+numbers[j]
            if (sumi == target):
                return [i+1,j+1]
            if (sumi > target):
                j-=1
            else:
                i+=1
        return [-1,-1]