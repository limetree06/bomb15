#include "IntArray.h"
#include <iostream>
using namespace std;

IntArray::IntArray(int n){
        int i;
        elements = new int[n];
        nelements =0;
        if (n!=0){
        for(i=0; i<n; i++)
            elements[i] = 0;}
        }

 IntArray::IntArray(const IntArray &obj){
        int i;
        elements = new int[obj.nelements];
        nelements = obj.nelements;
        for (i=0; i < nelements; i++){
            elements[i]=obj.elements[i];}
        }
IntArray::~IntArray(){ delete []elements;}

int IntArray::pop(){
            int i, pop;
            int wow[nelements];
            pop = elements[0];
            for(i=0; i <(nelements-1); i++)
                wow[i] = elements[i+1];

            delete []elements;
            elements = new int[--nelements];

            for( i=0; i<nelements; i++)
                elements[i] = wow[i];
		
		return pop;
            }

bool IntArray::empty() const{
        if (nelements == 0) return true;
        else return false;
        }

int IntArray::top() const{
        int top;
        if (nelements == 0){
            cout << "Error: invalid memory access" <<endl;
                return 1;}

        else {top = elements[0];
                return top;}}

void IntArray::push(int number){
        int i;
        int num[nelements];
        if (nelements == 0) {
                delete [] elements;
                elements = new int[++nelements];
                elements[0] = number;}

        else {
            for(i = 0; i < nelements; i++)
                num[i] = elements[i];
		
            delete [] elements;

            elements = new int[++nelements];
            for(i=0; i<(nelements-1); i++)
                elements[i+1]= num[i];

            elements[0] = number;

   }

    }

int& IntArray::operator[](int index){
            if (index <0 || index >= 100){
                cout << "Error: invalid memory access" <<endl;}

            return elements[index];
            }

IntArray& IntArray::operator=(const IntArray& arr){
        int i;
        if( &arr != this){
            delete []elements;
            nelements=arr.nelements;
            elements = new int[nelements];

        for(i=0; i < nelements; i++)
            elements[i] = arr.elements[i];
        }
        return *this;
    }

void IntArray::appendCopyAtEnd(const IntArray& arr){
        int i;
        int num[nelements];
        for (i=0; i<nelements; i++)
            num[i]=elements[i];

        delete []elements;
        elements = new int[arr.nelements + nelements];

        for (i=0; i<nelements; i++)
            elements[i]=num[i];


        for(i=0; i< arr.nelements; i++){
            elements[i+nelements]=arr.elements[i];
        }
	nelements += arr.nelements;}

//
