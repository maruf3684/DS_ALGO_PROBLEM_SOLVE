// p:=30
// q:=&p

// fmt.Println(p)
// fmt.Println(q)

///////////////////////////////////////////

package main

import (
	"fmt"
)

func main() {
	p:=30
	var q *int=&p
    
	//////////////////////
	fmt.Println(p)
	*q=90
	fmt.Println(p)

	fmt.Println(*q-1)

	fmt.Println(q)


////////////////////////////////////////////////////////////////

var munna [10]int=[10]int{2,4,5,67,4,5,6,4,55,4}

var ptr *[10]int = &munna

 fmt.Print(*ptr)

///////////////////////////////////////////////////

var ptr2 *int = &munna[0]

fmt.Println(ptr2)


// for i := 0; i < 10; i++ {
// 	var ir *int = &i
// 	fmt.Println((*ptr2+*ir))
	
// }

/////////////////////////////////////////////




}