
//rotate matrix
//[[1, 2],[3, 4]] main arr
//[[3, 4], [1, 2]] After rotation
//[[3, 1],[4, 2]]  final
/////////////////////////////////////////////////////////////////////////

function myrotation(Arr){
    Arr=Arr.reverse();
    for (let i = 0; i < Arr.length; i++) {
        for (let j = 0; j <  i; j++) {
            
           [ Arr[i][j],Arr[j][i] ] = [ Arr[j][i],Arr[i][j] ]
            
        }   
    }
        
   
    return Arr
}



console.log(myrotation([
    [1, 2],
    [3, 4]
]))

