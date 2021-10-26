
let arr=[6,33,23,5,52,3]


function swap(arr,one,two){
    let temp=arr[one];
    arr[one]=arr[two];
    arr[two]=temp;
}

function partition(arr,min,max){
let start=min;
let end=max;
let pivot=arr[Math.floor((min + max) / 2)]



while(start<=end){

while(arr[start]<=pivot){
    start++
}

while(arr[end]>pivot){
    end--
}

if(start<=end){
    swap(arr,start,end)
    start++;
    end--;
}
}
return start;

}


function quickSort(arr,min,max){
    var index;
    if(arr.length>1){
        index=partition(arr,min,max);

        if(min<index-1){
            quickSort(arr,min,index-1)
        }
        if(index<max){
            quickSort(arr,index,max)
        }
    }
    return arr;
}



console.log(quickSort(arr,0,arr.length - 1));