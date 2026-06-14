class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      
        c1 = c2 = None
        n1 = n2 = 0

        for x in nums:
            if x == c1:
                n1 += 1
            elif x == c2:
                n2 += 1
            elif n1 == 0:
                c1, n1 = x, 1
            elif n2 == 0:
                c2, n2 = x, 1
            else:
                n1 -= 1
                n2 -= 1

        res = []
        for c in [c1, c2]:
            if nums.count(c) > len(nums) // 3:
                res.append(c)

        return res