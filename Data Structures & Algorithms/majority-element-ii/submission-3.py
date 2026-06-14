class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        threshold = len(nums) // 3
        return [k for k, v in counts.items() if v > threshold]