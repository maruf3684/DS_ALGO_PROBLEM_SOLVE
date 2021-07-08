
#include<iostream>
#include<stdlib.h>
  
using namespace std;
  

void add(int *&c,int b){
   
   
   int newvalu=10;
   c=&newvalu;

   int d= *c+b;
   cout<<d<<endl;

}

  
int main(){

int a=2;

int b=4;

int *c=&a;

add(c,b);

////////////////////////////////////////////////////////////////
int one=1;
int two=2;

int three=3;



int sum= one + two;

cout<<sum;

return 0;
}