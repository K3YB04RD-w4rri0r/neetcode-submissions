class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        while True:
            for word in strs:
                if not word.startswith(prefix):
                    prefix = prefix[:-1]
                    break
            else:
                return prefix