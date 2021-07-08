//!foreatch

let arr=[2,3,5,33,2,5,44,66,43,23]


let contain=arr.forEach(function (element,index,array){
    console.log(`element = ${element} index = ${index} array = ${array}`);
    return array;  /// RETURN UNDEFINED
})

console.log(contain);


////! Make OWN FOREACH

function loop(arr,callback){
    for (let index = 0; index < arr.length; index++) {
        callback(arr[index])
    }
}

//lets call function
loop(arr,function callback(i){
    console.log("ellement =",i);});







