class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        _map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in _map.keys():
                if stack == [] or _map[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return stack == []
        