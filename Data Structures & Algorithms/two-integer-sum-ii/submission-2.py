class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0,len(numbers) - 1
        s = numbers[i] + numbers[j]
        while s != target:
            if s > target:
                j -= 1
            else:
                i += 1
            s = numbers[i] + numbers[j]
        return [i + 1, j + 1]