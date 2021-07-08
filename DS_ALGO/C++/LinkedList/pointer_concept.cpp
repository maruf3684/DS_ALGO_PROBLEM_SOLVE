#include <iostream>
using namespace std;





int main(){
    

    int munna=4;
    
    int *munnaaddress = &munna;
    cout<<munnaaddress<<endl;
    cout<<*munnaaddress<<endl;

    cout<<"................................"<<endl;
    cout<<*munnaaddress<<endl;

    int** munnaaddress2= &munnaaddress;
    cout<<munnaaddress2<<endl;

    int*** munnaaddress3=&munnaaddress2;
    cout<<munnaaddress3<<endl;

    cout<<"................................"<<endl;
    cout<<***munnaaddress3<<endl;

    cout<<"................................"<<endl;
    cout<<*&munna<<endl;
 
  cout<<"............. null valu..................."<<endl;
   
   int *head=NULL;
   cout<<head<<endl;
   cout<<*&head<<endl;
   cout<<&head<<endl;
   //cout<< *head; neba na

     cout<<"............. with value mofo..................."<<endl;
   
   int mofo=2;
   int *head2=&mofo;

   cout<<head2<<endl;
   cout<<*&head2<<endl;
   ///////////////////////////////////
    cout<<" *&head2 mane address er adderss er value=address"<<endl;
   cout<<head2<<endl;
   cout<<&head2<<endl;
   cout<<*&head2<<endl;
   //////////////////////////////////////
    cout<<" *&head2 mane address er adderss er value=address"<<endl;
   cout<< *head2;
    
  

    return 0;
}

    // int munna=4;
    // int* munnaaddress = &munna;
    // cout<<munnaaddress<<endl;
    // cout<<&munnaaddress;
 