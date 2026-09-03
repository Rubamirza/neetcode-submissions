from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 0
            
            hash_map[nums[i]] += 1
        
        sorted_hashmap = dict(sorted(hash_map.items(), key=itemgetter(1), reverse=True))

        
        res = []
        for key in sorted_hashmap:
            res.append(key)
            if len(res) == k:
                break
        
        return res
            


        