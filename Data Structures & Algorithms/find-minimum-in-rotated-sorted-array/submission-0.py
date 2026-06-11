class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            me = nums[mid]
            re = nums[r]
            if me > re:
                l = mid+1
            else:
                r = mid
            

        return nums[l]
