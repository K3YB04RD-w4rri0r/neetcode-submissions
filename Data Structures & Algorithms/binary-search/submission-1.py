class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l < r:
            midpoint = l + (r - l) // 2
            # print(midpoint)
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                l = midpoint + 1
            else:
                r = midpoint


        return l if nums[l] == target else -1