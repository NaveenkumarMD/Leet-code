const currarrsum=(arr,s)=>{
    let startindex=0
    let endindex=0
    let currsum=0
    let n=arr.length
    for(let i=0;i<n;i++){
        while(currsum>s && startindex<i-1){
            currsum-=arr[startindex]
            startindex++
        }
        if(currsum===s){
            return [startindex,endindex]
        }
        if (currsum<s){
            currsum+=arr[i]
            endindex++
        }
    }
    return [0]
}
let x=currarrsum([1, 4, 20, 3, 10, 5],33)
console.log(x)
