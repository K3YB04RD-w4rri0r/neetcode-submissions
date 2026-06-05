class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            n = nums[i]
            p1, p2 = i + 1, len(nums) - 1

            while p1 < p2:
                n1, n2 = nums[p1], nums[p2]
                if n1 + n2 < -n:
                    p1 += 1
                elif  n1  + n2 == -n:
                    s = [nums[i], nums[p1], nums[p2]]
                    print(s)
                    if s not in out:
                        out.append(s)
                    p1 += 1
                else:
                    p2 -= 1
        return out
