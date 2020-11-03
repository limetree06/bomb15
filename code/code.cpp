#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

int main(){
	srand(time(NULL));
	int i,  block[62];
	
	for(i=0; i<62 ; i++){
		block[i] = rand()%62+1;}



	for (i=0; i<62; i++) cout << i<< block[i]<< endl;

return 0;}
