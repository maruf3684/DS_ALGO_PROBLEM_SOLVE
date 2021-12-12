


// function trailing_Zero(n){
//     count = 0
//     for (let i=5; i<=n; i=i*5)
//         count = count+n/i
//     return Math.floor(count)

// }

// console.log(trailing_Zero(32))

//with while loop

//sutro=(n/5)+(n/25)+(n/125)+(n/625)

let n=32
let count = 0
i=5

while(n>=i){
    count=count+n/i
    i=i*5
}

console.log(Math.floor(count));