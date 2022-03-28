"""
Find duplicates within a range `k` in an array
Given an array and a positive number k, check whether the array contains any duplicate elements within the range k.
 If k is more than the array’s size, the solution should check for duplicates in the complete array.
"""
def findduplicates(nums, k):
    dit={}
    for i in range(len(nums)):
        if nums[i] in dit:
            if abs(dit[nums[i]]-i)<=k:
                return True
        dit[nums[i]]=i
    return False

x = findduplicates([5, 6, 8, 8, 4, 6, 9], 4)
print(x)
