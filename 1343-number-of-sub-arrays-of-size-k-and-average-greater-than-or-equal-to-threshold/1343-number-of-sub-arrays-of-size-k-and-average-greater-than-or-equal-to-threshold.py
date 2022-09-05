class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        s=sum(arr[:k])
        if s//k >=threshold:
            count=1        
        for i in range(1,len(arr)-k+1):
            s-=arr[i-1]
            s+=arr[i+k-1]
            avg=s//k
            if avg>=threshold:
                count+=1
        return count