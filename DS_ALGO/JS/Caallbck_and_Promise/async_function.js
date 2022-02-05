
const myFunc = async () => {
    console.log("inside myfunc");
    let i=0;
    while (true) {
        i=i+1;
       if(i===1000000000){
           break;
       }
    }
    return 'Hello+World';
};

let result = myFunc();

result.then((data) => {
    //paoua data diye ja iccha koro
    console.log(data);
});

//or

const myFunc2 = async () => {
    let data=await myFunc();
      //paoua data diye ja iccha koro
    console.log(data);
}

myFunc2();