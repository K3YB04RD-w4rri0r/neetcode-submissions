class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        for i in range(len(s)):
            p1 = 0
            p2 = 0
            substring = set()
            while 0 <= i - p1 and i + p2 < len(s):
                if s[i - p1] not in substring:
                    substring = substring | {s[i - p1]}
                    p1 += 1
                elif s[i + p2] not in substring:
                    substring = substring | {s[i + p2]}
                    p2 += 1
                else:
                    break
                
            l = max(l, len(substring))

        return l


