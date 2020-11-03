#include <iostream>
#include "IntArray.h"
using namespace std;

void empty(IntArray& il) {
    while(!il.empty())
        il.pop();
    }

int main(){

	cout<<"-------------------- test 1 -----------------"<< endl;
	IntArray s1;
	for(int i = 0; i < 10; i ++)
		s1.push(i);

	cout<<s1<<endl; 
	for(int i = 0 ;  i < 10; i++)
		s1[i] = i;

	cout<<s1<<endl;
    
	IntArray s2(s1);
	empty(s1);
	s1.appendCopyAtEnd(s2); //appended by an empty list
	cout<<s1<<endl;

    empty(s1);
    empty(s2);
    s1.push(10);
    s1.push(20);
    s2.push(30);
    s2.push(40);
    s1.appendCopyAtEnd(s2);
    cout << s1 << endl;
    empty(s1);
    s1.push(10);
    s1.push(20);
    s2.appendCopyAtEnd(s1);
    cout << s2 << endl;

	s1[100] = 100;
	IntArray s3;
	        s3.push(5);
	            s3 = s3;
	                cout << s3 << endl;
	                    IntArray s4;
	                        IntArray s5;
	                            s5 = s3;
	                                cout << s5 << endl;
	
	                                   cout << endl << endl << endl;
	                                        IntArray s6;
	                                           s6.push(7);
	                                                cout << s6.pop();
	                                                    s6.push(8);
	                                                        cout << s6.pop();
	
	                                                            cout << endl;
	                                                                cout <<s1 << endl;
	                                                                   cout <<s1[2] << endl;
	                                                                        cout << s1[1] << endl;
	                                                                            IntArray s7;
	                                                                                s7.push(10);
	                                                                                    cout << s7[0] << endl;
	                                                                                        cout << s7.top() << endl;
                                                                                           s7.pop();
	                                                                                                cout << s7[0] << endl;
	
	                                                                                                    IntArray s9;
	                                                                                                        for(int j = 0; j < 100; j++)
	                                                                                                            {
	                                                                                                                    s9.push(j);
	                                                                                                                        }
	                                                                                                                            for(int j = 0; j < 5; j ++)
	                                                                                                                                {
	                                                                                                                                        s9.pop();
	                                                                                                                                            }
	                                                                                                                                                cout << s9 << endl;
	                                                                                                                                                    IntArray s10 = s9;
	                                                                                                                                                        s9.appendCopyAtEnd(s10);
	                                                                                                                                                            IntArray s11;
	                                                                                                                                                                s11 = s9;
	                                                                                                                                                                    cout << s11 << endl;
	                                                                                                                                                                    }
