class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size <= 2:
            return []
        nums.sort()
        ans = []
        i = 0
        while i < size:
            if i == 0 or nums[i] != nums[i - 1]:
                element = nums[i]
                target = 0 - element
                pairs = self.twoSum(nums, i + 1, size - 1, target)
                for pair in pairs:
                    ans.append([element, pair[0], pair[1]])
            i += 1
        return ans   
    
       
    def twoSum(self, nums, start, end, target):
        f = start
        s = end
        pairs = []
        while f < s:
            if f - 1 >= start and nums[f] == nums[f - 1]:
                f += 1
                continue
            if s + 1 <= end and nums[s] == nums[s + 1]:
                s -= 1
                continue
            sum = nums[f] + nums[s]
            if sum < target:
                f += 1
            elif sum > target:
                s -= 1
            elif sum == target:
                pairs.append([nums[f], nums[s]])
                f += 1
        return pairs
        
        
        