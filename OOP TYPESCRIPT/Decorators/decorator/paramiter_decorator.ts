export {};

function ParamDecorator(
	target: any,
	propertykey: string,
	parameterIndex: number
) {
	console.log(target);
	console.log(propertykey);
	console.log(parameterIndex);
	console.log(".......................");
	
}

class Tool {

	public name: string;

	constructor(name: string) {
		console.log("constractor called");

		this.name = name;
	}

	price(): void {
		console.log("$200");
	}

	print(@ParamDecorator isTrue:string,printNumber:number): void {
		console.log(isTrue);
	}
}

const tool = new Tool("hammer");

tool.print("yes",10)


