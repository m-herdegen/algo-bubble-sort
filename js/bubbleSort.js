var arr = [4, 3, 5, 0, 1]
var swaps = 0

// Your Code Here
let previous = arr[0]
let current = arr[1]
let looping = true 

while(looping){
    let swapped = false 
    for(i = 0; i < arr.length -1; i++){
        previous = arr[i]
        current = arr[i + 1]
        if(previous > current){
            swapped = true
            swaps += 1
            arr[i] = current
            arr[i+1] = previous 
        }
    }
    if(!swapped){
        looping = false
    }
}


const result = arr

console.log("Final result: " + result)
console.log("Swaps: " + swaps)
