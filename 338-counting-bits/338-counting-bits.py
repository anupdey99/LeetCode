class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(self.getNumOfSetBits(i))
        return result
    
    def getNumOfSetBits(self, num: int) -> int:
        count = 0
        for i in range(32):
            if (num & (1<<i)) > 0:
                count += 1
        return count