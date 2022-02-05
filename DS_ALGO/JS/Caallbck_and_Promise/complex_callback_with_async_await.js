console.log("start");

function getParam(name) {
	return new Promise((resolve, reject) => {
		setTimeout(function () {
			console.log("inside timeout");

			resolve("md." + name);
		}, 2000);
	});
}

function getParam2(fullname) {
	return new Promise((resolve, reject) => {
		setTimeout(function () {
			console.log("inside timeout 2");

			resolve(["coading", "cricket"]);
		}, 2000);
	});
}

function getParam3(hobby) {
	return new Promise((resolve, reject) => {
		setTimeout(function () {
			console.log("inside timeout 3");

			resolve("selected in varsity");
		}, 2000);
	});
}

async function call() {
try{
    const name="munna"
	const fullname = await getParam(name);
	console.log(fullname);
	const hobby = await getParam2(fullname);
	console.log(hobby);
	const result = await getParam3(hobby);
	console.log(result);
}catch(err){
    console.log(err);
}

}
call();
console.log("end");
