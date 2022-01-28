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
    
    //"module": "es6" or "commonJS" in tsconfig.ts// comon js korle node a ts chole But browser a cholche na 
    // "type": "module", packge.json a korle module system import export node a chole
    // <script src="./decorator.js" type="module" defer></script> in html a korle es6 export bujhe