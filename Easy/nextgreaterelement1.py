from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict={}
        for i,j in enumerate(nums2):
            dict[j]=i
        print(dict)
        arr=[-1 for _ in range(len(nums1))]
        for i,k in enumerate(nums1):
            if k in dict:
                for j in range(dict[k],len(nums2)):
                    if list(dict.keys())[j]>k:
                        arr[i]=list(dict.keys())[j]
                        break
        return arr


x=Solution()
y=x.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
print(y)