#include <iostream>
#include <fstream>
#include<string>
#include<vector>
#include <math.h>
#include<chrono>
using namespace std;

int main() {
	string num;
	ifstream read("input.txt");
	vector <int> matrix;
	int i, j, k, done;

		if (read.is_open()){
			while (!read.eof()){
				read >> num;
				matrix.push_back( stoi(num) );
			}
			read.close();
		}
	
		chrono::system_clock::time_point StartTime = std::chrono::system_clock::now();
		int N = sqrt(matrix.size() / 2);
		int *value = new int[N*N];
		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) {
				done = 0;
				for (k = 0; k < N; k++) {
					done = done + matrix[i*N + k] * matrix[N*N+ j + N * k];
				}
				value[i*N+j] = done;
			}
		}

		chrono::system_clock::time_point EndTime = std::chrono::system_clock::now();
		chrono::nanoseconds nano = EndTime - StartTime;
		cout << nano.count() << endl;

		ofstream write;
		write.open("output.txt");
		if (write.is_open()) {
			for (i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					write << value[i*N + j] << " ";
				}
				write << endl;
			}
		}write.close();


	return 0;
}
