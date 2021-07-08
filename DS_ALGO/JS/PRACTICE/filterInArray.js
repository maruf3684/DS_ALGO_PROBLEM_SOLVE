arr=[
    {name:"munna",age:20},
    {name:"neon",age:21},
    {name:"siam",age:22},
]

witharrobj=arr.filter((obj)=>{
    return obj.age ===20;
})

console.log(witharrobj);

//!//////////////////////////////////////

witharrobj2=witharrobj.values();

for (const value of witharrobj2) {
    console.log(value);
  }
  

//////////////////////////////////////

console.log("new",witharrobj[0]);

////////////////////////////////////////

console.log("///////////////");

for (const value of arr.values()) {
    console.log(value);
  }
  