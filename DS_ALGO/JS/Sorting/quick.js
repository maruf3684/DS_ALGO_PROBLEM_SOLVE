


// var items = [6,33,23,5,52,3]
// function swap(items, leftIndex, rightIndex){

//     var temp = items[leftIndex];
//     items[leftIndex] = items[rightIndex];
//     items[rightIndex] = temp;
// }


// function partition(items, left, right) {
//     var pivot   = items[Math.floor((right + left) / 2)] //middle element
//         let i       = left //left pointer
//         let j       = right; //right pointer

//     while (i <= j) {
//         while (items[i] < pivot) {
//             i++;
//         }
//         while (items[j] > pivot) {
//             j--;
//         }
//         if (i <= j) {
//             swap(items, i, j); 
//             i++;
//             j--;
//         }
//     }
//     return i;
// }

// function quickSort(items, left, right) {
//     var index;
//     if (items.length > 1) {
//         index = partition(items, left, right); 

//         if (left < index - 1) { 
//             quickSort(items, left, index - 1);
//         }
//         if (index < right) { 
//             quickSort(items, index, right);
//         }
//     }
//     return items;
// }

// var sortedArray = quickSort(items, 0, items.length - 1);
// console.log(sortedArray); 




// let arr=[6,33,23,5,52,3]


// function swap(arr,one,two){
//     let temp=arr[one];
//     arr[one]=arr[two];
//     arr[two]=temp;
// }

// function partition(arr,min,max){
// let start=min;
// let end=max;
// let pivot=arr[Math.floor((min + max) / 2)]



// while(start<=end){

// while(arr[start]<=pivot){
//     start++
// }

// while(arr[end]>pivot){
//     end--
// }

// if(start<=end){
//     swap(arr,start,end)
//     start++;
//     end--;
// }
// }
// return start;

// }


// function quickSort(arr,min,max){
//     var index;
//     if(arr.length>1){
//         index=partition(arr,min,max);

//         if(min<index-1){
//             quickSort(arr,min,index-1)
//         }
//         if(index<max){
//             quickSort(arr,index,max)
//         }
//     }
//     return arr;
// }



// console.log(quickSort(arr,0,arr.length - 1));