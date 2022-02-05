
console.log("start");

function getParam(name) {
setTimeout(function() {
    console.log("inside timeout");
    return name;
},2000)
}

let get=getParam("munna")
console.log(get);

console.log("end");

//output
//start
//undefined
//end
//inside timeout