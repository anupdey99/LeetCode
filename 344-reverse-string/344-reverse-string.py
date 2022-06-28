class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        # pointer O(n) O(1)
        # idx1 = 0
        # idx2 = n - 1
        # while idx1 < idx2:
        #     temp = s[idx2]
        #     s[idx2] = s[idx1]
        #     s[idx1] = temp
        #     idx1 += 1
        #     idx2 -= 1 
        
        # another approch
        for i in range(0, (n//2)):
            s[i], s[n-1-i] = s[n-1-i], s[i]