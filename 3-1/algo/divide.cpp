#include <iostream>
#include <fstream>
#include<string>
#include<vector>
#include<math.h>
#include<chrono>
using namespace std;
int *matrix1, *matrix2;
int N;
int MatMult(int[], int, int, int, int);

int main() {
	vector <int> matrix;
	string num;
	ifstream read("input.txt");
	int i;

	if (read.is_open()) {
		while (!read.eof()) {
			read >> num;
			matrix.push_back(stoi(num));
		}
		read.close();
	}

	chrono::system_clock::time_point StartTime = std::chrono::system_clock::now();

	N = sqrt(matrix.size() / 2);
	matrix1 = new int[N*N];
	matrix2 = new int[N*N];
	int *value = new int[N*N];

	for (i = 0; i < N*N; i++) {
		matrix1[i] = matrix[i];
		matrix2[i] = matrix[i + N * N];
		value[i] = 0;
	}

	i = MatMult(value, 0, 0, N, 0);

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

	delete[] matrix1;
	delete[] matrix2;
	delete[] value;

	return 0;
}

int MatMult(int value[], int a, int b, int n, int index) {

	if (n == 1) { return matrix1[a] * matrix2[b]; }

	if (n != 1) {
		value[index] += MatMult(value, a, b, n / 2, index) + MatMult(value, a + n / 2, b + N * n / 2, n / 2, index);
		value[index + n / 2] += MatMult(value, a, b + n / 2, n / 2, index + n / 2) + MatMult(value, a + n / 2, b + N * n / 2 + n / 2, n / 2, index + n / 2);
		value[index + N * n / 2] += MatMult(value, a + N * n / 2, b, n / 2, index + N * n / 2) + MatMult(value, a + N * n / 2 + n / 2, b + N * n / 2, n / 2, index + N * n / 2);
		value[index + N * n / 2 + n / 2] += MatMult(value, a + N * n / 2, b + n / 2, n / 2, index + N * n / 2 + n / 2) + MatMult(value, a + N * n / 2 + n / 2, b + N * n / 2 + n / 2, n / 2, index + N * n / 2 + n / 2);
	}

	return 0;
}
