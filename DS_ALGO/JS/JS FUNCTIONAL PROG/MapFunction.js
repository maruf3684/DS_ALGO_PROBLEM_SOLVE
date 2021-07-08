//array element ke 2 kore increase koro

let array=[5,9,6,1,2,4,5,6]


// let newarray=[]
// for (let index = 0; index < array.length; index++) {
//       newarray.push(array[index]+2)
    
// }

// console.log(newarray);

//!map function
// let newarray=array.map((value)=>{
//     return value+2;
// })
// console.log('====================================');
// console.log(newarray);
// console.log('====================================');

//!lets make own map functional


function mymap(array,callback){
    newarray=[]
    for (let index = 0; index < array.length; index++) {
        newarray.push(callback(array[index],index))
    }
    return newarray;
}

newmakedarray=mymap(array,function callback(value,index){
    return value+2
})

console.log(newmakedarray);