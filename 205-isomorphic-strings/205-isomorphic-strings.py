class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            if charS not in sMap:
                sMap[charS] = charT
            if charT not in tMap:
                tMap[charT] = charS
            if (sMap[charS] != charT or tMap[charT] != charS):
                return False
        return True
        