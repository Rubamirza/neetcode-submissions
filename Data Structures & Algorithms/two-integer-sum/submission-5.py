class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force: O(n^2)
        #for i in range(len(nums)):
            #for j in range(i+1,len(nums)):
                #if nums[i] + nums[j] == target:
                    #return [i,j]
            
        #HASHMAP??
        hash_map = {}
        for i in range(len(nums)):
            answer = 0
            answer = target - nums[i]
            if answer not in hash_map:
                hash_map[nums[i]] = i
            else:
                return [hash_map[answer], i]
