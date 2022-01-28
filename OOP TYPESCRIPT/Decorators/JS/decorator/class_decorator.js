var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
function CarDecorator(constructor) {
    constructor.prototype.date = new Date();
    constructor.prototype.giveMeDate = function () {
        return this.date;
    };
}
let Car = class Car {
    // then you can use this operator.
    constructor(brand) {
        this.brand = brand;
    }
};
Car = __decorate([
    CarDecorator
], Car);
const car = new Car("Ford");
const car1 = new Car("Tata");
console.log(car.brand);
console.log(car1.brand);
console.log(car.date);
console.log(car.giveMeDate());
//Lets make another class
let Bus = class Bus {
};
Bus = __decorate([
    CarDecorator
], Bus);
const bus1 = new Bus();
console.log("date for bus", bus1.date);
export {};
