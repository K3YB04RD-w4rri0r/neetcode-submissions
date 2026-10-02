class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        # window = []
        window_sum = 0
        min_size = float("+inf")
        while l <= r < len(nums):
            #window.append(nums[r])
            # print(window)
            # if sum(window) < target:
            window_sum += nums[r]
            # print(l, r, window_sum, min_size)
            if window_sum < target:
                # print(True)
                r += 1
            else:
                # print(False)
                min_size = min((r - l + 1), min_size)
                window_sum -= nums[l]
                window_sum -= nums[r]
                l += 1
                
                # window = window[1:]
        return 0 if min_size == float("+inf") else min_size
        


