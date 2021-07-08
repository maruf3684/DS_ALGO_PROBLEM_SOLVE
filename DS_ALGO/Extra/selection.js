arr=[10,6,93,2,5,2];

for (var i=0;i<=arr.length-2;i++){
    var cont=i;
    for (var j=i+1;j<=arr.length-1;j++){
        if(arr[cont]>arr[j]){

            cont=j;
            
        }
    }
    var temp=arr[cont]
    arr[cont]=arr[i]
    arr[i]=temp;
   
}
console.log(arr);

