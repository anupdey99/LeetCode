class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        pos = len(digits) - 1
        while digits[pos] == 9:
            digits[pos] = 0
            pos -= 1
        if digits == [0] * len(digits):
            digits = [1] + [0] * len(digits)
        else:
            digits[pos] += 1
        return digits