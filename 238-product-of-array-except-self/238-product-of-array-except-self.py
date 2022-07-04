class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        left = [1]
        right = [1] * (n+1)
        # print(left, right)
        for i in range(1, n):
            left.append(left[i-1] * nums[i-1])
            # print(left)
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        for i in range(n):
            result.append(left[i] * right[i])
        return result