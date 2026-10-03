class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rgb = { 0: [],
                1 : [],
                2 : []}
        for i in nums:
            rgb[i].append(i)

        nums[:] = rgb[0] + rgb[1] + rgb[2]
