
function maxarr(arr) {
    let max_so_far = -Infinity
    let max_here = 0
    arr.forEach(element => {
        max_here += element
        if (max_here > max_so_far) {
            max_so_far = max_here
        }
        if (max_here < 0) {
            max_here = 0
        }
    })
    return max_so_far
}
let arr = [-2, -3, 4, -1, -2, 1, 5, -3]
let x = maxarr(arr)
console.log(x)


const r=new Promise((resolve,reject)=>{
    
})
