class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer_j = 0 
        for i in range(len(nums)):
            pointer_j += 1
            for j in range(pointer_j,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            

        
        