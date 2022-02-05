console.log("start");

function getParam(name, callback) {
	setTimeout(function () {
		console.log("inside timeout");
		 callback("md." + name);
	}, 2000);
}

function getParam2(fullname, callback) {
	setTimeout(function () {
		console.log("inside timeout 2");
		 callback(["coading", "cricket"]);
	}, 2000);
}

function getParam3(hobby, callback) {
	setTimeout(function () {
		console.log("inside timeout 3");
		return callback("selected in varsity");
	}, 2000);
}

let get = getParam("munna", (fullname) => {
	console.log(fullname);
	getParam2(fullname, (hobby) => {
		console.log(hobby);
		getParam3(hobby, (result) => {
			console.log(result);
		});
	});
});

console.log("end");
