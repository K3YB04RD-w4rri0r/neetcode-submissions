class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dnums = {str(nums[i]) : i for i in range(len(nums)) }
        print(dnums)
        for i in range(len(nums)):
            current_num = int(nums[i])
            print(current_num)
            compl = target - current_num
            print(compl)
            if str(compl) in dnums:
                if dnums[str(compl)] != i: 
                    return [i, dnums[str(compl)]]

        return []
        