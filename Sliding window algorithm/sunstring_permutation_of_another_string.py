"""
Find all substrings of a string that are a permutation of another string
Find all substrings of a string that contains all characters of another string.
 In other words, find all substrings of the first string that are anagrams of the second string.
"""
def findanagrams(s,x):
    i=0
    k=len(x)
    count=0
    while i<len(s)-len(x)+1:
        temp=s[i:i+k]
        if sorted(temp)==sorted(x):
            count+=1
        i+=1
    return count

x=findanagrams("XYYZXZYZXXYZ","XYZ")
print(x)