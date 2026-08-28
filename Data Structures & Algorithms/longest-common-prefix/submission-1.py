class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for j, char in enumerate(strs[0]):
            for i in range(1,len(strs)):

                if j >= len(strs[i]) or strs[i][j] != char:
                    return output
            output += char    
        return output
                
                    






        

        