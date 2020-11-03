#ifndef INTARRAY_H_INCLUDED
#define INTARRAY_H_INCLUDED
#include <iostream>
using namespace std;

class IntArray{
private:
    int nelements;
    int *elements;

public:
    IntArray(int n=0);
    IntArray(const IntArray &obj);
    ~IntArray();
    int pop();
    bool empty() const;
    int top() const;
    void push(int number);
    int& operator[](int index);
    IntArray& operator=(const IntArray& arr);
    void appendCopyAtEnd(const IntArray& arr);
    int getLength()const{return nelements;}
    friend ostream& operator <<(ostream& os, const IntArray& arg){
        for(int i = 0; i < arg.nelements; i++){
                os<<arg.elements[i]<<' ';
        }
        return os;}};

#endif 
