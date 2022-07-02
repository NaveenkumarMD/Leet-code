function findmissing(arr){
    let actual=arr[0];
    for(let i=1;i<arr.length;i++){
        actual=actual^arr[i]
    }
    let curr=1;
    for(let i=2;i<=arr.length+1;i++){
        curr=curr^i
    }
    return curr^actual

}
x=findmissing([1,2,3,4,5,6,8])
console.log(x)