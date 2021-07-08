package main

import (
	"fmt"
	
)

func main() {
	var munna[4][4] int = [4][4]int {{1,2,3,4},{12,13,14,5},{11,16,15,6},{10,9,8,7}}
	fmt.Println(munna)

	for i := 0; i < len(munna); i++ {
		for j := 0; j < len(munna); j++ {
			fmt.Print(munna[i][j]," ")
		}
		fmt.Println()
	}

////////////////////////////////////////////////////////////////

var colstart int =0
var colend int =3

var rowstart int =0
var rowend int =3


for(colstart<=colend){

for i := colstart; i<= colend; i++ {
	fmt.Print(munna[rowstart][i]," ")
}
rowstart =rowstart+1

for i := rowstart; i <= rowend; i++ {
	fmt.Print(munna[i][colend]," ")
}
colend=colend-1


for i := colend; i>= colstart; i-- {
	fmt.Print(munna[rowend][i]," ")
}

rowend = rowend-1

for i := rowend; i>= rowstart; i-- {
	fmt.Print(munna[i][colstart]," ")
}
colstart=colstart+1

}

}