"""
Find the longest substring of a string containing `k` distinct characters
Given a string and a positive number k, find the longest substring of the string containing k distinct characters. 
If k is more than the total number of distinct characters in the string, return the whole string
"""
def longestsunstring(s,k):
    low=high=0
    end=begin=0
    window=set()
    freq={chr(97+i):0 for i in range(26)}
    while high<len(s):
        window.add(s[high])
        freq[s[high]]+=1
        while len(window)>k:
            freq[s[low]]-=1
            if freq[s[low]]==0:
                window.remove(s[low])
            low+=1
        if end-begin<high-low:
            end=high
            begin=low
        high+=1
    return s[begin:end+1]
s = 'abcbdbdbbdcdabd'
k = 2
x=longestsunstring(s, k)
print(x)