from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dit1={chr(i):0 for i in range(97,97+26)}
        dit2={chr(i):0 for i in range(97,97+26)}
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            dit1[s1[i]]+=1
            dit2[s2[i]]+=1
        i=0
        while i<len(s2)-len(s1):
            if dit1==dit2:
                return True
            dit2[s2[i+len(s1)]]+=1
            dit2[s2[i]]-=1
            i+=1
        return dit1==dit2
        
            
            