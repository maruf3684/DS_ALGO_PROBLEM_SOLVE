
#include <iostream>
using namespace std;


class student{

      public:
      string name;
      int age;
      bool gender;

      //!default constrattor
      student(){
          cout << "default constractor called"<<endl;
      }
      
       //!paramiterized constrattor
      student(string nameq, bool genderq,int ageq){
          cout << "paramitarized constractor called"<<endl;
          name=nameq;
          age=ageq;
          gender=genderq;
      }


      //!copy constrattor
      student(student &a){
          cout << "copy constractor called"<<endl;
          name=a.name;
          age=a.age;
          gender=a.gender;
      }


      //!destractor

      ~student(){
          cout<<"dstractor called"<<endl;
      }
      

      void printInfo(){
        cout << "Name ";
        cout<<name<<endl;
        cout << "Age ";
        cout<<age<<endl;
        cout << "Gender ";
        cout<<gender<<endl;

    }

};


int main(){
    

     //!paramiterized constrattor call hobe
    student Munna("munna",1,22);
    Munna.printInfo();
    
    
     //!default constrattor call hobe
    student Soyeb;

    //!Copy constractor cal hobe

    student Nahid=Munna;
    Nahid.printInfo();
    
    
    
    
  return 0;
}