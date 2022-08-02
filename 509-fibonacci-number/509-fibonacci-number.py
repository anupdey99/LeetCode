class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        pre = 0
        curr = 1
        next = 0
        count = 1
        while count < n:
            next = pre + curr
            pre = curr
            curr = next
            count += 1
        return curr
        
        