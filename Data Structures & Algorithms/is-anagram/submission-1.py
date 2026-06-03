class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted([l for l in s])
        t = sorted([l for l in t])

        return t == s 