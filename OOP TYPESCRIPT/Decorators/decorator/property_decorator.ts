export {};

function NameDecorator(
	target: any,
	propertykey: string,
) {
	console.log(target);
	console.log(propertykey);
	//descriptor.writable=false
	//decorator.js:29 Uncaught TypeError: Cannot assign to read only property 'print' of object '#<Tool>'
}

class Tool {
	@NameDecorator
	public name: string;
	
	constructor(name: string) {
		console.log("constractor called");
		
		this.name = name;
	}

	price(): void {
		console.log("$200");
	}


	print(): void {
		console.log("Printing tool");
	}
}

const tool = new Tool("hammer");
console.log(tool.name);

