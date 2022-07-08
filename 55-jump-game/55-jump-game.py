class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = nums[0]
        i = 1
        while(i < len(nums)) and maxJump >= i:
            if (i + nums[i] > maxJump):
                maxJump = i + nums[i]
            i += 1
        
        if (maxJump >= (len(nums) - 1)):
            return True
        else:
            return False
            