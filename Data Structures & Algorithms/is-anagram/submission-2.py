class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dt = {}
            ds = {}
            for i in range(len(s)):
                ds[s[i]] = ds.setdefault(s[i], 0) + 1
                dt[t[i]] = dt.setdefault(t[i], 0) + 1
            return dt == ds 