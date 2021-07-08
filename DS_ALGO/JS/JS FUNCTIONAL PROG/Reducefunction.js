let array=[5,9,6,1,2,4,5,6]

//// ! value gula jog koro/gun koro


// let sum=0;

// for (let index = 0; index < array.length; index++) {
//     sum = sum+ array[index];
    
// }

// console.log(sum);


let newarray=array.reduce(function(a,b){
    return a*b;
})
console.log(newarray);