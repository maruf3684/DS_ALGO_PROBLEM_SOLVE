//!2// 2ta class bind korte//or inherite krte



// function Person(){
//     this.name="Munna"
// }

// function Student(){
//     Person.call(this)
//     this.subject="javascript"
// }

// var student1=new Student();
// var student2=new Person();

// console.log(student1.name)
// console.log(student2.name);




function Person(name){
    this.name=name;
}
Person.prototype.print=function(){
    console.log(this.name);
}

//

function Student(name,sub){
    Person.call(this,name)
    this.subject=sub
}
Student.prototype=Object.create(Person.prototype)
console.log(Student.prototype===Person.prototype);
Student.prototype.constructor=Student

//or

//Object.setPrototypeOf(Student.prototype,Person.prototype)
//Student.prototype.constructor=Student



student1=new Student("munna","js")
student1.print()

console.log(Student.prototype===Person.prototype); 
console.log(student1 instanceof Person);
console.log(student1 instanceof Student);


//! //prototype copy holo referance copy
//! change korlam person a impacr porlo Studen er object e
Person.prototype.print=function(){
    console.log(this.name,"version 2");
}
student1.print()