let promisify = require("util").promisify;

function getParam(name, callback) {
	setTimeout(function () {
		console.log("inside timeout");
       
		callback(null, "md." + name); //kaj sesh a callback ke call kore deca
	}, 2000);
}

//i can do this

getParam("munna", (optional,fullname) => {
    console.log("ja data pailam ta niye kaj korbo aikhane");
	console.log(fullname);
	console.log("end-----------");
});
console.log("..........................................");

//or this



let promise = promisify(getParam);

//callback ar code akhon likhbo aikhane mane then er moddhe
promise("munna")
	.then((fullname) => {
        console.log("ja data pailam ta niye kaj korbo aikhane");
		console.log(fullname);
		console.log("end-----------");
	})
	.catch((err) => {
		console.log(err);
	});
console.log("..........................................");

//or i can do this

async function something(name) {
	try{
		let fullname = await promise(name);
		 console.log("ja data pailam ta niye kaj korbo aikhane");
		 console.log(fullname);
		 console.log("end-----------");
	}catch(err){
		console.log(err);
	}
}

something("munna");

console.log("..........................................");
