//implicit binding
//explicit binding
//new binding
//window binding


//!implicit binding

// let sakib={
//     name:"sakib",
//     age:30,
//     printplayerName:function(){
//         console.log(this.name);
//     }
// }

// sakib.printplayerName()



//! / ////////////////////////////2/////////////////////////////////////////

// let sakib={
//         name:"sakib",
//          age:30,
//         }

// let tamim={
//         name:"tamim",
//          age:20,
//         }

// let printPlayernameFunction = function(obj){       /// object a value dhukanor function
//     obj.printPlayername=function print (){
//         console.log(this.name);
//     }
// }

// printPlayernameFunction(tamim)                      /// object a value dhukalam
// printPlayernameFunction(sakib)

// tamim.printPlayername()                            //dhukano function ke call korlam
// sakib.printPlayername() 

//* sakib.printPlayername()  sakib call koreche mane . er age sakib ache ty this keyword sakib ke point korbe




//!explicit binding


// printPlayername=function(v1,v2){
//     console.log(`name: ${this.name} ${v1} ${v2}`);
// }


// let sakib={
//         name:"sakib",
//         age:30,
// }

// //.call() received other paramiter too

// let v1="good looking";
// let v2="all rounder"

// // printPlayername.call(sakib,v1,v2)

// // let v3=[v1,v2]

// // printPlayername.apply(sakib,v3)   // .apply array hesaba pathai


// //? now .bind()

// let letsCallNow=printPlayername.bind(sakib,v1,v2)   //bind auto call kore na .call or .apply er moto
// letsCallNow()

///* alada context ar method ke alada alada context a use korte bind use hoi

//! ak context er mal arak context a dhukabo bind diye







////!new binding

// function person(name,age){
//?    // let this =Object.create(null) //Nul object create korche mon a mon a
//     this.name=name;                  //object a value vorce
//     this.age=age;                     //object a value vorce       
    
//?     //return this// notun create kora object ta ke return kore deccha

//     console.log(`${this.name} is ${age} old`);
// }

//   sakib =new person("sakib,20");  //new keyword use korar fol e uporer moto hosse


////!Window binding

//"use strict"

// let printname=function(){
//     console.log(this===global);
//     console.log(this.name);
// }

// let sakib={
//     name:"sakib"
// }

// printname()