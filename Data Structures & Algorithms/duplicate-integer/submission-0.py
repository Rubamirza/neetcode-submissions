class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = {}
        for i in range(len(nums)):
            new_list[nums[i]] = new_list.get(nums[i], 0) + 1
            if new_list[nums[i]] == 2:
                return True
            
    
        return False
        