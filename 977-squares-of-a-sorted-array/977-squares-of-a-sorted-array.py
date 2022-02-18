class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numbers = [x**2 for x in nums]
        numbers.sort()
        return (numbers)