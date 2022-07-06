class Solution:
    def climbStairs(self, n: int) -> int:
        self.map = {}
        return self.step(0, n)
        
    def step(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        if i in self.map:
            return self.map[i]
        self.map[i] = self.step(i + 1, n) + self.step(i + 2, n)
        return self.map[i]
        