#include<iostream>

using namespace std;

int main(){
	int a,i, num=0, put=0;
	int back, sip, il;
	int regist[10], input[50], count[50];
	do{
		cin >> a ;
	}while(a<1);

	cout << endl;
	
	do{
		cin >> input[num];
	}while(input[num++]==100);
	
	do{
		cin >> input[put];
	}while(input[put++]==100);

	for (i=0; i=< put; i++){
		back= (input[i]/100);
		sip = ((input[i]%100)/10);
		il = (input[i]%10);
		switch(back)
	{	
		case 1:
		case 2:
		case 3:
		case 4:
		case 5:
		case 6:
		case 7:
		case 8:
		case 9:
		case 0:
	}
}

		
return 0;}

