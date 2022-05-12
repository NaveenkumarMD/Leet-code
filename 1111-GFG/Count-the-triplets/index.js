function binarysearch(arr,x){
    let start=0
    let end=arr.length
    let mid
    while (start<=end){
        mid=parseInt((start+end)/2)
        if(arr[mid]==x){
            return true
        }
        else if (arr[mid]<x) {
            start=mid+1
        }
        else{
            end=mid-1
        }
    }
    return false
}
function tripletsum(arr){
    arr.sort()
    let count=0
    for(let i=0;i<arr.length-1;i++){
        for(let j=i+1;j<arr.length;j++){
            if(binarysearch(arr,arr[i]+arr[j])){
                count+=1
            }
        }
    }
    return count
}
x=[2,3,4,4,5,6,4636,643,34,23,53,26,34,6,234,4,4,4,43,4,2,3,2,3]
console.log(tripletsum(x))