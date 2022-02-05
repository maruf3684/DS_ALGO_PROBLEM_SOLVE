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

const get1 = getParam("munna");

get1
	.then((fullname) => {
		console.log(fullname);
		return getParam2(fullname);
	})
	.then((hobby) => {
		console.log(hobby);
		return getParam3(hobby);
	})
	.then((result) => {
		console.log(result);
	})
	.catch((err) => {
		console.log(err);
	});

console.log("end");
