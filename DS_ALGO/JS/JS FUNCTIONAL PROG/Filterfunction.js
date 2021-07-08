
let array=[5,9,6,1,2,4,5,6]

// //!lets find even number

// let newarray=[]
// for (let index = 0; index < array.length; index++) {
//     if (array[index]%2==0) {
//         newarray.push(array[index])
//     }
      
// }

// console.log(newarray);

// //!lets find even number with filterfunction

// let newarray=array.filter((value)=>{
//      return value%2==0;
// })

// console.log(newarray);

// //!lets find even number with  own filterfunction



function myfilter(array,callback){
     let newarray=[]
     let k;
    for (let index = 0; index < array.length; index++) {
        k=callback(array[index])
        if(k){
            newarray.push(k)
        }

        
    }
     return newarray;
}


collectedarray=myfilter(array, function callback(value){
    if(value%2==0){
        return value                      //we can return true false by 
                                                        // return value%2==0   //true na hole false return hobe
                                                        //aita diye uporer functiona a kaj kora jabe
    } 
} )

console.log(collectedarray);