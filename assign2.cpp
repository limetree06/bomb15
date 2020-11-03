#include <iostream>

using namespace std;

int main(){
        int a, i, count;
        int num =0;
        int back, sip, il;
        int regist[10], input[50], RAM[50];
        char ch1, ch2;
        do{
                cin >> a;
        }while(a < 1);

        do{
                cin >> input[num];

        }while (input[num++]!=100);

  


        count = 0;
        for(i=0; i <= num; i++){
                back = (input[i]/100);
                sip = ((input[i] %100)/10);
                il = (input[i]%10);
                count ++;
                switch (back)
        {
                case 2: regist[sip] = il;
                case 3: {regist[sip] += il;
                        regist[sip] = (regist[sip]%1000);
                        }
                case 4:{ regist[sip] *= il;
                        regist[sip] = (regist[sip]%1000);
                        }
                case 5: {regist[il] = regist[sip];
                        regist[sip] = (regist[sip]%1000);
                        }
                case 6: {regist[il] += regist[sip];
                        regist[sip] = (regist[sip]%1000);
                        }
                                       

                case 7: {regist[il] *= regist[sip];
                        regist[sip] = (regist[sip]%1000);
                        }
                case 8: input[il] = regist[sip];

                case 9: regist[sip] = input[il];
                case 0:{
                        if(regist[il] !=0);
                        i = regist[sip];}

                case 1: i = num+1;


}}


                cout << count << endl;




return 0;
}

