#include <iostream>
using namespace std;

int main(){

    int a=5;
  
    
    for (int i = a; i >=1 ; i--)
    {
    for (int j = 1; j <=i ; j++)
    {
        cout<<"* ";
    }
        cout<<endl;
    }


    return 0;
}