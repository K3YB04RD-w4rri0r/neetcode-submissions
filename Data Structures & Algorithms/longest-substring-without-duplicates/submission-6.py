class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l = 0
        L = 0
        R = 0
        seen = set()
        while R < len(s):
            if s[R] in seen:
                l = max(l, R - L)
                seen.discard(s[L])
                L = L+1
            else:
                seen.add(s[R])
                R += 1
        l = max(l, R - L)

        return l


