class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        shortest_word = min(strs, key=len)
        for i in range(len(shortest_word)):
            if all([x.startswith(shortest_word[:i+1]) for x in strs]):
                prefix = shortest_word[:i+1]
            else:
                break
        return prefix