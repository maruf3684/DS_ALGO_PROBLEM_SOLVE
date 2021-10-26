

//ak context er sathe onno context ke badhe deta bind call apply use kora hoi


function print(a,b){
    console.log(a+b+this.c);
}

obj1={
    c:2
}


// print2=print.bind(obj1);
// print2(1,1)



//print.call(obj1,1,1);



print2=print.apply(obj1,[1,1]);