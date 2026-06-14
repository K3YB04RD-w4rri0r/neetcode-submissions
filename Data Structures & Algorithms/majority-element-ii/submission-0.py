class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        over = set()
        for e in nums:
            count = counts.get(e, 0) + 1
            counts[e] = count
            if count > int(len(nums)/3):
                over.add(e)



        return list(over)