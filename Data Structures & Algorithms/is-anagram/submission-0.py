class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}
        
        for char in s:
            if char not in hash_map_s:
                hash_map_s[char] = 1
            else:
                #count_s += 1
                hash_map_s[char] +=1
        for char in t:
            if char not in hash_map_t:
                hash_map_t[char] = 1
            else:
                #count_t += 1
                hash_map_t[char] +=1
        
        if hash_map_s == hash_map_t:
            return True
        else:
            return False

            

                
        
        