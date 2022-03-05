class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dit={x:-1 for x in nums2}
        for i in range(len(nums2)-1):
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    dit[nums2[i]]=nums2[j]
                    break
        return [dit[i] for i in nums1]
        