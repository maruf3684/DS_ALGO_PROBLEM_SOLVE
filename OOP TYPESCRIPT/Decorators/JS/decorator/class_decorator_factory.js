var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
function CarDecorator(constructor) {
    console.log("CarDecorator invoked");
    constructor.prototype.date = new Date();
    constructor.prototype.giveMeDate = function () {
        return this.date;
    };
}
function OtherDecorator(name) {
    console.log("factory called");
    return function (constructor) {
        console.log("OtherDecorator invoked");
        constructor.prototype.other = name;
    };
}
let Car = class Car {
    constructor(brand) {
        this.brand = brand;
    }
};
Car = __decorate([
    OtherDecorator("Other"),
    CarDecorator
], Car);
const car = new Car("Ford");
console.log(car.other);
export {};
