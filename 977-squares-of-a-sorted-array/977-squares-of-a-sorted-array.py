class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0 for _ in nums]
        smallIdx = 0
        largeIdx = len(nums) - 1
        for i in reversed(range(len(nums))):
            smallValue = nums[smallIdx]
            largeValue = nums[largeIdx]
            if abs(smallValue) > abs(largeValue):
                result[i] = smallValue ** 2
                smallIdx += 1
            else:
                result[i] = largeValue ** 2
                largeIdx -= 1
        return result
        
        