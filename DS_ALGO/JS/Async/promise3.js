
promise1=Promise.resolve("promise 1 done");

promise2=new Promise((resolve,reject) =>{
    setTimeout(()=>{
        resolve("promise 2 done")
    },2000)
})

Promise.all([promise1,promise2]).then((resolveDone)=>{
    console.log(resolveDone);
})

Promise.race([promise1,promise2]).then((resolveDone)=>{
    console.log(resolveDone);
})