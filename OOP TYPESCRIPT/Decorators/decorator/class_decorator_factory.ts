export {};

function CarDecorator(constructor: Function) {
    console.log("CarDecorator invoked");
    
    constructor.prototype.date=new Date()
    constructor.prototype.giveMeDate= function(){
        return this.date
    }
}


function OtherDecorator(name:string){
    console.log("factory called");
    return function (constructor: Function) {
        console.log("OtherDecorator invoked");
        constructor.prototype.other=name
      }
}



@OtherDecorator("Other")
@CarDecorator
class Car {
	public brand: string;
    public date!: Date;                     //There will be a scenario when TypeScript believes that certain property, 
    public giveMeDate!: Function;            //variable will be null or undefined. But if you are sure that this variable cannot be null,
    public other!:string                                        // then you can use this operator.
	constructor(brand: string) {
		this.brand = brand;

	}
}

const car = new Car("Ford");

console.log(car.other);

