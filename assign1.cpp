//ces24101, cs20171143, sonminji

#include <iostream>
using namespace std;

char  mat[50][20];
char find_word[20][20];

int check_left(int i, int j, int k);
int check_right(int i, int j, int k);
int check_up(int i, int j, int k);
int check_down(int i, int j, int k);
int check_rightup(int i, int j, int k);
int check_rightdown(int i, int j, int k);
int check_leftup(int i, int j, int k);
int check_leftdown(int i, int j, int k);

int main()
{
	int a, s, j, i, k, left, down, num_word;
	do {
		cin >> a;
	}while(a<1);

	cout << endl;
	
	cin >> left >> down;
	for(i=0; i<left; i++){
		for (j=0; j<down; j++){
			cin >> mat[i][j];
			if(mat[i][j] >='A' && mat[i][j] <='Z'){
				mat[i][j] = mat[i][j] +32;
	}}}

	cin >> num_word;

	for(i=0; i<num_word ; i++){
		cin >> find_word[i];}
	
	for(i=0; i<num_word; i++){
		for(j=0; j < find_word[i][j] == '\0'; j++){
			if(find_word[i][j] >= 'A' && find_word[i][j] <='Z'){
				find_word[i][j] = find_word[i][j] +32;}}}
					
		
	for(i=0; i<num_word; i++){
		for(j=0; j<left; j++){
			for(k=0; k<down; k++){
				if(mat[j][k]==find_word[i][0]){
					if ( check_left(i,j,k)== 0) break;
					else if ( check_right(i,j,k) == 0) break;
					else if ( check_up(i,j,k) == 0) break;
 					else if ( check_down(i,j,k) == 0) break; 
					else if ( check_rightup(i,j,k) == 0) break; 
					else if ( check_leftup(i,j,k) == 0) break;
					else if ( check_rightdown(i,j,k) == 0) break;
					else if ( check_leftdown(i,j,k) == 0) break;
					else continue;
	

}}}}
return 0;
}


int check_left(int i, int j, int k){
	int s, num=0;
	for (s=0; s<100; s++){
		if(find_word[i][s] != '\0') 
			num=s+1;
		else break;
}	for (s=0; s< num; s++){
		if(mat[j][k+s] == find_word[i][s]){
			if(find_word[i][s+1]=='\0'){
				cout << j+1  <<" " << k+1 << endl;
				return 0;}
}
		
		else return 1;}
}


int check_right(int i, int j, int k){
	int s, num=0;
        for (s=0; s<100; s++){
                if(find_word[i][s] != '\0')
                        num=s+1;
		else break;
}
        for (s=0; s< num; s++){
                if(mat[j][k-s] == find_word[i][s]){
			if(find_word[i][s+1] =='\0') {
			cout << j+1 << " " << k+1 << endl;
                        return 0;}
}

                else return 1;
}}


int check_up(int i, int j, int k){
        int s, num=0;
        for (s=0; s<100; s++){
                if(find_word[i][s] != '\0')
                        num=s+1;
		else break;
}

        for (s=0; s< num =='\0'; s++){
                if(mat[j+s][k] != find_word[i][s]){
			if(find_word[i][s+1] =='\0') {
                        cout << j+1 << " " << k+1 << endl;
                        return 0;}
}

                else return 1;
}}


int check_down(int i, int j, int k){
        int s, num=0;
        for (s=0; s<100; s++){
                if(find_word[i][s] != '\0')
                        num=s+1;
		else break;
}

        for (s=0; s< num =='\0'; s++){
                if(mat[j-s][k] != find_word[i][s]){
			if(find_word[i][s+1] =='\0') {
                        cout << j+1 << " " << k+1 << endl;
                        return 0;}}


                else return 1;
}}


int check_rightup(int i, int j, int k){
        int s, num=0;
        for (s=0; s<100; s++){
                if(find_word[i][s] != '\0')
                        num=s+1;
		else break;
}

        for (s=0; s< num =='\0'; s++){
                if(mat[j+s][k+s] != find_word[i][s]){
			if(find_word[i][s+1] =='\0') {
                        cout << j+1 << " " << k+1 << endl;
                        return 0;}
}

                else return 1;
}}


int check_rightdown(int i, int j, int k){
        int s, num=0;
        for (s=0; s<100; s++){
                if(find_word[i][s] != '\0')
                        num=s+1;
		else break;
}

        for (s=0; s< num =='\0'; s++){
                if(mat[j-s][k+s] != find_word[i][s]){
                       if(find_word[i][s+1] =='\0') {
                       cout << j+1 << " " << k+1 << endl;
                       return 0; 
 }

}
                else return 1;
}}


int check_leftup(int i, int j, int k){
        int s, num=0;
        for (s=0; s<100; s++){
                if(find_word[i][s] != '\0')
                        num=s+1;
		else break;
}

        for (s=0; s< num =='\0'; s++){
                if(mat[j+s][k-s] != find_word[i][s]){
			if(find_word[i][s+1] =='\0') {
                        	cout << j+1 << " " << k+1 << endl;
                        	return 0;}
}

                else
                        return 1;
}}


int check_leftdown(int i, int j, int k){
        int s, num=0;
        for (s=0; s<100; s++){
                if(find_word[i][s] != '\0')
                        num=s+1;
		else break;
}

        for (s=0; s< num =='\0'; s++){
                if(mat[j-s][k-s] != find_word[i][s]){
			if(find_word[i][s+1] == '\0'){
				cout << j+1 << " " << k+1 <<endl;
				return 0;}}
			
                else return 1;
}}

