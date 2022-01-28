var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
function ParamDecorator(target, propertykey, parameterIndex) {
    console.log(target);
    console.log(propertykey);
    console.log(parameterIndex);
    console.log(".......................");
}
class Tool {
    constructor(name) {
        console.log("constractor called");
        this.name = name;
    }
    price() {
        console.log("$200");
    }
    print(isTrue, printNumber) {
        console.log(isTrue);
    }
}
__decorate([
    __param(0, ParamDecorator)
], Tool.prototype, "print", null);
const tool = new Tool("hammer");
tool.print("yes", 10);
export {};
