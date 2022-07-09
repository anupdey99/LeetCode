class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        maxProd = 0
        currentProd = 1
        
        for i in nums:
            if i == 0:
                currentProd = 1
            else:
                currentProd *= i
                maxProd = max(maxProd, currentProd)
        
        currentProd = 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                currentProd = 1
            else:
                currentProd *= nums[i]
                maxProd = max(maxProd, currentProd)
        
        return maxProd