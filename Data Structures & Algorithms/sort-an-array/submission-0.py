class Solution:
    def separate(self, arr):
        # print(arr)
        if arr == []:
            return [], [] 

        mid = len(arr) // 2
        # print(arr[:mid], arr[mid:])
        return arr[:mid], arr[mid:]

    def fusion(self, arr1, arr2):
        a1, a2 = arr1, arr2
        out = []
        while a1 and a2:
            if a1[0] <= a2[0]:
                out.append(a1[0])
                a1 = a1[1::]
            else:
                out.append(a2[0])
                a2 = a2[1::]

        out += a1 + a2
        return out


    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums

        a1, a2 = self.separate(nums)
        return self.fusion(self.sortArray(a1), self.sortArray(a2))

        
        