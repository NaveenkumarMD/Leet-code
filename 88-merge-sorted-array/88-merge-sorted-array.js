/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1,m,nums2,n){
    i=m-1
    j=n-1
    k=m+n-1
    while (i>=0 && j>=0){
        if (nums1[i]>nums2[j]){
            nums1[k]=nums1[i]
            i--
        }
        else{
            nums1[k]=nums2[j]
            j--
        }
        k--
    }
    while(i>=0){
        nums1[k]=nums1[i]
        k--
        i--
    }
    while(j>=0){
        nums1[k]=nums2[j]
        k--
        j--
    }
}