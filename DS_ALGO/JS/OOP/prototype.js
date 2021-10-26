
// function Person(name,age){
//     this.name=name;
//     this.age=age;
//     this.hello=function(){
//         console.log("hellow",this.name);
//     }
// }

////////////////////////////////////////////

// function Person(name,age){
//     this.name=name;
//     this.age=age;
// }

// Person.prototype.hello=function(){
//     console.log("hellow",this.name);
// }

//! prototype is allso a object
function Person(name,age){
    this.name=name;
    this.age=age;
}

Person.prototype={
    hello:function(){
    console.log("hellow",this.name);
}
}





//! ////////////////////////////////////////////////////////
var p1=new Person("maruf hasan",22)
var p2=new Person("modi",10)

console.log(p1);
console.log(p2);

console.log(p1.__proto__==p2.__proto__); 



//!  /////////////Aktar proto change korle ar akter proto change hoi///prototype is shared 
p1.__proto__.married="yes"
console.log(p2.married);

//! ajob jinish niche 
console.log(Person.prototype);
console.log(p1.__proto__);
console.log(p1.prototype);
console.log(Person.__proto__);

console.log(p1.constructor);
console.log(Person.constructor);