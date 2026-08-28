class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans_size = 2 * len(nums)
        ans = [0] * ans_size
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        
        return ans