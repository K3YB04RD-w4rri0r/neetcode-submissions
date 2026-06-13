class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        target_index = -1
        """
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
        """

        while l <= r:
            # print(l)
            # print(r)
            mid = l +  (r - l) // 2
            # print(mid)
            # print("-")
            # print(nums[l] <= nums[mid])
            if nums[l] <= nums[mid]:
                if nums[mid] == target:
                    return mid
                elif nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1

            else:
                if nums[mid] == target:
                    return mid
                elif nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid

        return target_index


