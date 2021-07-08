#include <iostream>
using namespace std;


class student{

    //private 
      string name;
      
      public:
      
      int age;
      bool gender;

//!for privates members only///they can not access from outside of class
      //!set methods

      void setName(string val){
          name=val;
      }

      void getName(){
          cout<<name<<endl;
      }

      //!getname


      void printInfo(){
        cout << "Name ";
        getName();
        
  

        cout << "Age ";
        cout<<age<<endl;


        cout << "Gender ";
        cout<<gender<<endl;

    }

};


int main(){

    // student a;
    // a.name = "Munna";
    // a.age= 20;
    // a.gender=1;


    //!Using array of objects to

    //!type/jaiga/jaigar moddher mal
    student munna[3];

    for (int i = 0; i < 3; i++)
    {
        cout << "Name ";
        string s;
        cin >> s;
        munna[i].setName(s);

        cout << "Age ";
        cin >> munna[i].age;

        cout << "Gender ";
        cin >> munna[i].gender;
    }

    for (int i = 0; i < 3; i++)
    {
        munna[i].printInfo();
    }
    
    
  return 0;
}