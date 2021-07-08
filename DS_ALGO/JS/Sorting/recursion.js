
// count n number

let total=0;
counting=(n)=>{
    total=total+1;
    if (total >= n){
        return total;
    }
    counting(n);
};

console.log(counting(6));