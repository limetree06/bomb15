#include<iostream>
#include<stdlib.h>

using namespace std;

#define MAXDIGITS 10

class ReversibleInteger{
private :
	char digits[MAXDIGITS];
	int lastdigit;
	int number;
	int result;

public :
	ReversibleInteger(int n=0);
	ReversibleInteger reverse();
	ReversibleInteger add(ReversibleInteger arg);
	unsigned int getValue();
};

	ReversibleInteger :: ReversibleInteger(int n){
}
	ReversibleInteger ReversibleInteger :: reverse(){
		int check;
		ReversibleInteger one;
		one.number = number;
		one.result =0;
		one.lastdigit=0;
		while(1){
			one.result=0;
			check = one.number;

		while( check != 0){
			one.result = (one.result*10 + check%10);
			check = check/10;
			}

			if(one.result == one.number) break;
			else {one = one.add(one);	
				one.lastdigit++;	
}}
	cout << one.lastdigit << " " << one.number << endl;

	return one;



}
ReversibleInteger ReversibleInteger :: add(ReversibleInteger arg){
	int i=0;
	number = (number + result);
	arg.number = number;
	do{
		number = number/10;
		i++;
	}while(number ==0);
	if(i > 9){
		arg.number =0;
		arg.result=0;
		return arg;
		}
	else  return arg;


}

unsigned int ReversibleInteger :: getValue(){
	cin >> digits;
		number = atoi(digits);
		return number;
	}
		
int main(){
	ReversibleInteger one[100];
	int a,i, num[100];
	cin >> a;
	for(i=0; i<a; i++){
		num[i] = one[i].getValue();		
	}

	cout << endl;
	
	for(i=0; i<a; i++){
			one[i] = one[i].reverse();
}
return 0;}
