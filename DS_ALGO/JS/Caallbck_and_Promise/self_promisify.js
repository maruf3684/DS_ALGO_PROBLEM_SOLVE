function getFruits(callback) {
	let fruits = ["apple", "banana", "orange"];
	setTimeout(() => {
		callback(fruits); //ultimately resolve er moddhe fruts dhuktesa
	}, 1000);
}

//getFruits(console.log);

function promisify(getFruits) {
	return function () {
		return new Promise((resolve, reject) => {
			try {
				getFruits(resolve);
			} catch (e) {
				reject(e);
			}
		});
	};
}


const promise=promisify(getFruits);

promise().then((fruits) => {
    console.log("prapto folafol niye kaj");
    console.log(fruits);
});