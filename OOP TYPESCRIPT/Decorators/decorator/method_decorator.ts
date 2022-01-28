export {};

function PrintDecorator(
	target: any,
	propertykey: string,
	descriptor: PropertyDescriptor
) {
	console.log(target);
	console.log(propertykey);
	console.log(descriptor);
	//descriptor.writable=false
	//decorator.js:29 Uncaught TypeError: Cannot assign to read only property 'print' of object '#<Tool>'
}

class Tool {
	public name: string;
	constructor(name: string) {
		this.name = name;
	}

	price(): void {
		console.log("$200");
	}

	@PrintDecorator
	print(): void {
		console.log("Printing tool");
	}
}

const tool = new Tool("hammer");
tool.print();

tool.print = function () {
	console.log("something else");
};
tool.print();