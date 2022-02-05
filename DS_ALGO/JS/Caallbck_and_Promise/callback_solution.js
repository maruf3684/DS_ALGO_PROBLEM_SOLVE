console.log("start");

function getParam(name,callback) {
setTimeout(function() {
    console.log("inside timeout");
    return callback(name);
},2000)
}

let get=getParam("munna",(name)=>{console.log(name);
})

console.log("end");

//start
//end
//inside timeout
//munna