#ifndef __GENERICSET_H__
#define __GENERICSET_H__

#define MAX_ITEMS 30

#include <iostream>
using namespace std;

template <class T>
class GenericSet
{
        protected:
                int size;
                T values[MAX_ITEMS];

        public:
                GenericSet(){size =0;}
                virtual void Insert(T item)=0;
                virtual void Delete(T item)=0;
                void Clear();
                int GetSize();
                bool IsFull();
                bool IsEmpty();

                friend std::ostream& operator<<(std::ostream& out, const GenericSet& s){
                        out << "{";
                        for(int i=0;i<s.size;i++){
                                out << s.values[i] ;
                                if(i < s.size-1) out << ", ";
                        }
                        out << "}";
                        return out;
                }
};

template <class T>
void GenericSet<T>::Clear(){
    for(int i=0; i < size; i++)
            values[i] = '\0';

size =0;}

template <class T>
int GenericSet<T>::GetSize(){return size;}

template <class T>
bool GenericSet<T>::IsFull(){
        if(size == 30) return true;
        else return false;}

template <class T>
bool GenericSet<T>::IsEmpty(){
        if(size ==0) return true;
        else return false;
                    }


template <class T>
class Set : public GenericSet<T>
 {    public :
        virtual void Insert(T item){
            int sizeone = GenericSet<T>::size;
            if(GenericSet<T>::size == 0) {GenericSet<T>::values[0] = item; GenericSet<T>::size++;}

            else if(GenericSet<T>::IsFull() == true){
                throw "Set Exception: No more space";
            }

            else{
                for (int i=0; i < sizeone ; i++){
                        if(GenericSet<T>::values[i] == item) break;
                        if (i == (GenericSet<T>::size - 1)) GenericSet<T>::values[GenericSet<T>::size++] = item;
            }
}}

        virtual void Delete(T item){
            int sizeone = GenericSet<T>::size;
            int wow;
            if (GenericSet<T>::IsEmpty() == true) throw "Set Exception: Not found";
            else {
                for(int i=0; i<sizeone ; i++){
                    if(GenericSet<T>::values[i] == item) { wow =i; break; }}

                for(int i=wow; i<sizeone-1; i++){
                    GenericSet<T>::values[i]=GenericSet<T>::values[i+1];}
                GenericSet<T>::size--;}}
};

template <class T>
class Bag : public GenericSet<T>
{    public :
        virtual void Insert(T item){
            if(GenericSet<T>::IsFull()==true){
                throw "Bag Exception: No more space";
            }

            else GenericSet<T>::values[GenericSet<T>::size++] = item;

        }

        virtual void Delete(T item){
            int sizeone = GenericSet<T>::size;
            int wow;
            if (GenericSet<T>::IsEmpty()==true){
                throw  "Bag Exception: Not found";
            }

            else{
                for(int i=sizeone; i>-1 ; i--){
                    if(GenericSet<T>::values[i] == item) { wow =i; break; }}

                for(int i=wow; i<sizeone-1; i++){
                    GenericSet<T>::values[i]=GenericSet<T>::values[i+1];}
                    GenericSet<T>::size--;}}
};




#endif
