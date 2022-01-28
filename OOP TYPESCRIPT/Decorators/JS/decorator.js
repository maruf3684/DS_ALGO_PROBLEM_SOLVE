var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
function CarDecorator(constructor) {
    console.log("--decorator invoked");
    console.log(constructor);
}
let Car = class Car {
    constructor(brand) {
        this.brand = brand;
        console.log("--constractor invoked");
    }
};
Car = __decorate([
    CarDecorator
], Car);
const car = new Car("Ford");
console.log(car.brand);
export {};
