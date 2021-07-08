// #include <iostream>
// using namespace std;

// int main(){



//     return 0;
// }

#include <iostream>
using namespace std;


class node{

    public:
    int data;
    node *next;
    node(int val){
        data = val;
        next = NULL;
    }

};



void insertAtTail(node *&head ,int val){

  cout<<"i am insert *&head/head "<<*&head<<endl;


   node *n =new node(val);
   cout<<"object toiri hosse"<<endl;
   cout<<"i am  n "<<n<<endl;
   cout<<"i am  n data "<<n->data<<endl;    //null next soho mal baniye dessi
   cout<<"i am  n next "<<n->next<<endl;
   cout<<"object toiri done"<<endl;

   if(head == NULL){
    cout<<"Akhon amar head null"<<endl;
     head=n;         //first call er pore theke head er man change
     cout<<"1st head a  akta object dhukalam "<<head<<endl;
     cout<<"1st head ar data = "<<head->data<<endl;
     cout<<"1st head ar next = "<<head->next<<endl;
     cout<<"-------------------------------"<<endl;
     return ;   //aikhane e return hoye gase
   }


   ///2nd call theke cholbe
   
   cout<<"Akhon amar head null na"<<endl;
   node *temp= head;
   cout<<"Temp er moddhe head dhukalam"<<endl;

   while (temp->next != NULL){
       cout<<"3rd call e chole"<<endl;  
       cout<<temp<<endl;
       temp=temp->next;
       cout<<"temp=temp->next korlam"<<endl;
       cout<<temp<<endl;
   }
   
   
   temp->next=n;
   cout<<"temp er next a notun object lagiye delam"<<endl;

}



void display(node *head){
    //head hosse address,, ar amra jani address dhorte *veriablle lage ty node *head 
    // value initialize korba *veriable diye but kaj kam narachara korba variable diye
    cout<<"i am display head "<<head<<endl;
    node *temp = head;
    cout<<"i am display temp "<<temp<<endl;

    while(temp != NULL){
        // temp neza akta address tar data te ache akta value & next a ache next temp er address
        cout<<"data= "<<temp->data<<"( myaddress "<<temp<<")"<<"( next address "<<temp->next<<")"<<endl;
        temp=temp->next;
    }
}



int main(){
    
     node *head=NULL;  ///one time inisilize hobe pore change hobe
     cout<<"i am inisial head/*&head (address)"<<*&head<<endl;
     cout<<"i am inisial &head (address er address) "<<&head<<endl;
   //  cout<<"i am inisial *head "<<*head<<endl; kaj hoi na

   cout<<"-----------------------Insert-------------------------------"<<endl;
    cout<<"1st call"<<endl;
     insertAtTail(head,1);
     //first call er pore theke head er man change
      
     cout<<"2st call"<<endl;
     insertAtTail(head,2);
    
     cout<<"3st call"<<endl;
     insertAtTail(head,3);
      
     cout<<"4st call"<<endl;
     insertAtTail(head,4);
     

     cout<<"-----------------------DISPLAY-------------------------------"<<endl;
     cout<<"display er moddhe pathalam "<<head<<endl;
     display(head);

    return 0;
}

//first call object1 toiri
//2nd call object2 toiri kore object1->next er sathe object2 connect and temp ke point koranoo object2 te
// 3rd call object 3 toiri /// temp ke object 3 te point