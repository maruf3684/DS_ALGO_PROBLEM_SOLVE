export {};
function CarDecorator(constructor:Function){
    console.log("--decorator invoked");
    console.log(constructor);
    
    }
    
    
    @CarDecorator
    class Car{
        public brand:string
        constructor(brand:string){
            this.brand=brand
            console.log("--constractor invoked");
        }
    }
    
    const car=new Car("Ford")
    
    console.log(car.brand);