
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     
        hashmap_anagram = defaultdict(list)
        for i in range(len(strs)):
            generate_key = [0] * 26
            for char in strs[i]:
                #act
                #a, c, t
                generate_key[ord(char)-ord('a')] += 1
            
            key = tuple(generate_key)
            hashmap_anagram[key].append(strs[i])
        
        return list(hashmap_anagram.values())

            


                
        