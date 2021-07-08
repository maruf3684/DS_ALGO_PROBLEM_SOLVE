package main

import (
	"fmt"
	
)


func kuddus(apoin *int , bpoin *int){
    apoin,bpoin=bpoin,apoin

	fmt.Println(*apoin,*bpoin)

  

}

func main() {

	var a int =10
	var b int =30

	var apoin *int =&a
	var bpoin *int =&b
	fmt.Println(*apoin,*bpoin)
    kuddus(apoin , bpoin)



	//////////////////////////////////////////////////////
            //!/  DOUBLE POINTER
	m:=90
	n:=&m

	o:=&n
    fmt.Println()
	fmt.Println(m,*n,**o)


}