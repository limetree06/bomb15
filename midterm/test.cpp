#include<iostream>

using namespace std;
enum Discipline { ARCHEOLOGY, BIOLOGY, COMPUTER_SCIENCE }; 

class Person { 
protected: 
string name; 

public: Person() { 
setName(""); } 

Person(string pName) {

 setName(pName); }

 void setName(string pName) { 
name = pName; } 

string getName() {

 return name;}

 };
 
 class Faculty: public Person { 
private: 
Discipline department; 

public: Faculty (string fname, Discipline d) : Person(fname) 

{ department = d; 
} 

void setDepartment(Discipline d) {

 department = d; 

} 

Discipline getDepartment( ) { 

return department; }

 };
 
 class TFaculty:  public Faculty {
 
private: 
string title; 

public: 

TFaculty(string fname, Discipline d, string title) : 
Faculty(fname, d) { setTitle(title); } 

void setTitle(string title) { 

this->title = title; 

} 

string getName( ) { 

return title + " " + Person::getName();}

 };


const string dName[] = { "Archeology", "Biology", "Computer Science" }; 

int main() {  

TFaculty prof("Indiana Jones", ARCHEOLOGY, "Dr."); 

Faculty prof2("Indiana Jones", ARCHEOLOGY); 

cout << prof.getName() << " teaches " << dName[prof.getDepartment()] << "." << endl;

 cout << prof2.getName() << " teaches " << dName[prof2.getDepartment()] << "." << endl;


return 0;
}
