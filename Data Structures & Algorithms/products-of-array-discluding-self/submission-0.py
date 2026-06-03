class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_indexes = []
        
        for num in range(len(nums)):
            if nums[num] == 0:
                zero_indexes.append(num)
            else:
                product = product * nums[num]
 
        if len(zero_indexes) > 1 :
            return [0] * len(nums)

        elif  len(zero_indexes) == 1:
            output = [0] * len(nums)
            output[zero_indexes[0]] = product
            return output

        else:
            output = [int(product/nums[i]) for i in range(len(nums))]
            return output
            
        