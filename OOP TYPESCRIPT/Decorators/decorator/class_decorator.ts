export {};

function CarDecorator(constructor: Function) {
    constructor.prototype.date=new Date()
    constructor.prototype.giveMeDate= function(){
        return this.date
    }
}

@CarDecorator
class Car {
	public brand: string;
    public date!: Date;                     //There will be a scenario when TypeScript believes that certain property, 
    public giveMeDate!: Function;            //variable will be null or undefined. But if you are sure that this variable cannot be null,
                                             // then you can use this operator.
	constructor(brand: string) {
		this.brand = brand;

	}
}

const car = new Car("Ford");
const car1 = new Car("Tata");

console.log(car.brand);
console.log(car1.brand );



console.log(car.date);
console.log(car.giveMeDate());



//Lets make another class
@CarDecorator
class Bus{}

const bus1=new Bus()
console.log("date for bus",(<any>bus1).date);
