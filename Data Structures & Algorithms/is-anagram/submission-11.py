class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Essential guard clause
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # 2. Since lengths are equal, we can safely use one index for both
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # 3. Compare the full maps
        return countS == countT