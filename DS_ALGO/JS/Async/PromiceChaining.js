//! promise.then return a promise

function getUsername() {
	return new Promise((resolve, reject) => {
		resolve({ name: "munna" });
        //reject("I AM REJECT")
	});
}

function getAge(data) {
	return new Promise((resolve, reject) => {
		data = { ...data, age: 20 };
		resolve(data);
	});
}

function getDepertment(data) {
	return new Promise((resolve, reject) => {
		data = { ...data, depertment: "cse" };
		resolve(data);
	});
}

function getPhoneNumber(data) {
	return new Promise((resolve, reject) => {
		data = { ...data, phone: 45567 };
		resolve(data);
	});
}

function printinfo(data) {
	console.log(data);
}


getUsername().then(
    function(value) { /* code if successful */ console.log(value); },   //*resolve hole 1st function chole
    function(error) { /* code if some error */ console.log(error);}   //*reject value paile 2nd function chole
  ).catch(function(error){console.log(error);})  //* abar reject value paile hole .catch er moddhe akta function ota o chole




  //////////////////////////////////////////////////////////////////////////////////////////////
  getUsername()
  .then(getAge)
  .then(getDepertment)
  .then(getPhoneNumber)
  .then(printinfo);


//or

let getPromise1=getUsername().then(getAge)                                           
let getPromise2=getPromise1.then(getDepertment)    //* promise.then neja o new promice return kore
let getPromise3=getPromise2.then(getPhoneNumber)   //*promice retun korle tar sathe fer .then lagano jai    
//                                                 //* akmatro promise er pore e .then lagano somvob
let getPromise4=getPromise3.then(printinfo)

////////////////////////////////////////////////////////////////////////////////////

//!most importantly [promise.then()] er moddhe  jei function dei jamon [getUsername().then(getAge)] "getage deci"
//! oi getAge er paramiter [function getAge(data) {}] mane "data" holo promise resolve er data
//!
