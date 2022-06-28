class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        idx1 = 0
        idx2 = n - 1
        while idx1 < idx2:
            temp = s[idx2]
            s[idx2] = s[idx1]
            s[idx1] = temp
            idx1 += 1
            idx2 -= 1 
        
        