class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        d = {str(nums[i]) : i for i in range(n)}
        max_k = 0
        i = 0
        while i < n:
            k = 1
            while str(nums[i] + k) in d:
                k += 1

            max_k = max(k, max_k)
            i += 1

        return max_k
        
