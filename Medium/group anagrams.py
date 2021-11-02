from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dit={}
        for i in strs:
            f="".join(sorted(i))
            if f not in dit:
                dit[f]=[i]
            else:
                dit[f].append(i)
        print(dit)  
        print([i for i in dit.values()])        

        
        
x=Solution()
y=x.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])