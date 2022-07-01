class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        map = {}
        result = []
        
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        
        for i in nums1:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        
        for i in nums2:
            if i in map and map[i] > 0:
                result.append(i)
                map[i] -= 1
        return result
            
            
        