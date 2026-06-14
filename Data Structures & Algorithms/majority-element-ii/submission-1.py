class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for e in nums:
            counts[e] = counts.get(e, 0) + 1

        return [e for e in counts.keys() if counts[e] > len(nums) // 3]