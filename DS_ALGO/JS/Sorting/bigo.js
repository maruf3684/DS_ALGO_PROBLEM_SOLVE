const {performance} = require('perf_hooks');


counting=(param)=>{
    let total=0;
    for (let i = 0; i < param; i++) {
         total += i;
    }

    return total
}

let start=performance.now()
console.log(counting(100000000))
let end=performance.now()

console.log(`performance= ${(end-start)/1000}`)

