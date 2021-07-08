
function sayName(name){
    return "hallo"+ name;
}


//! Fun can be store in variable
a= sayName()
console.log(a);

b = sayName
console.log(b);
console.log(b("munna"))



console.log("///////////////////////////////////////////////////");


//! Fun can be store in Array

myarray=[1,2,3,4,b]

console.log(myarray[4]());


//! Fun can be store as an object field

let myobject={
    a:function(){
        console.log("i am stored in object");
    }
}

console.log(myobject.a); 
myobject.a()

//! We can create function as we need

console.log("///////////////////////////////////////////////////");

data=20+(function(){return 30})()
console.log(data);



console.log("///////////////////////////////////////////////////");

//!we can pass function as argument

function wow(name,great) {
    return great(name)
}

function great(name2) {
    return `wow ${name2} is great`
}

let store=wow("munna",great)

console.log(store);

//!we can return function from another functional

function base(a) {
    return function power(b){
        console.log("pre");
       var valu=1
       for (let i = 1; i <= b; i++) {
        console.log("middle");
           valu=valu*a
       }
       console.log("post");
       return valu
    }
}

// returnpower=base(10)
// console.log(returnpower(2));   or
console.log(base(10)(2))