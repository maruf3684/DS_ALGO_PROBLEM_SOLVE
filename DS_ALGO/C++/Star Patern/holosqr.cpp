#include <iostream>
using namespace std;

int main(){

    int a=4;
    int b=4;
    for (int i = 0; i <a ; i++)
    {
      for (int j = 0; j <b ; j++)
      {
         if (i==1 || i==2){
             if (j==1 || j==2)
             {
                cout<<"  ";
             }
            else{
           cout<<"* ";
           } 
   
         }
         else{
           cout<<"* ";
         }
         
     }

      
        cout<<endl;
    }


    return 0;
}