#include <iostream>
#include <fstream>
#include<string>
#include<vector>
#include <math.h>
#include<chrono>
using namespace std;

void add(const int[], const int[], int[]);
void sub(const int[], const int[], int[]);
void mul(const int[], const int[], int[]);
void C11(int[], int[], int[], int[]);
void C22(int[], int[], int[], int[]);
int N;

int main() {
	vector <int> matrix;
	string num;
	ifstream read("input.txt");
	int i, j;

	if (read.is_open()) {
		while (!read.eof()) {
			read >> num;
			matrix.push_back(stoi(num));
		}
		read.close();
	}

	chrono::system_clock::time_point StartTime = std::chrono::system_clock::now();
	N = sqrt(matrix.size() / 2);
	int *A11 = new int[N*N / 4];
	int *A12 = new int[N*N / 4];
	int *A21 = new int[N*N / 4];
	int *A22 = new int[N*N / 4];
	int *B11 = new int[N*N / 4];
	int *B12 = new int[N*N / 4];
	int *B21 = new int[N*N / 4];
	int *B22 = new int[N*N / 4];
	int *S1 = new int[N*N / 4];
	int *S2 = new int[N*N / 4];
	int *S3 = new int[N*N / 4];
	int *S4 = new int[N*N / 4];
	int *S5 = new int[N*N / 4];
	int *S6 = new int[N*N / 4];
	int *S7 = new int[N*N / 4];
	int *S8 = new int[N*N / 4];
	int *S9 = new int[N*N / 4];
	int *S10 = new int[N*N / 4];
	int *P1 = new int[N*N / 4];
	int *P2 = new int[N*N / 4];
	int *P3 = new int[N*N / 4];
	int *P4 = new int[N*N / 4];
	int *P5 = new int[N*N / 4];
	int *P6 = new int[N*N / 4];
	int *P7 = new int[N*N / 4];
	int *value = new int[N*N];

	for (i = 0; i < N / 2; i++) {
		for (j = 0; j < N / 2; j++) {
			A11[i*N / 2 + j] = matrix[i*N + j];
			A12[i*N / 2 + j] = matrix[N / 2 + i * N + j];
			A21[i*N / 2 + j] = matrix[N*N / 2 + i * N + j];
			A22[i*N / 2 + j] = matrix[N*N / 2 + N / 2 + i * N + j];
			B11[i*N / 2 + j] = matrix[N*N + i * N + j];
			B12[i*N / 2 + j] = matrix[N*N + N / 2 + i * N + j];
			B21[i*N / 2 + j] = matrix[N*N + N * N / 2 + i * N + j];
			B22[i*N / 2 + j] = matrix[N*N + N * N / 2 + N / 2 + i * N + j];
		}
	}

	sub(B12, B22, S1);
	add(A11, A12, S2);
	add(A21, A22, S3);
	sub(B21, B11, S4);
	add(A11, A22, S5);
	add(B11, B22, S6);
	sub(A12, A22, S7);
	add(B21, B22, S8);
	sub(A11, A21, S9);
	add(B11, B12, S10);

	mul(A11, S1, P1);
	mul(S2, B22, P2);
	mul(S3, B11, P3);
	mul(A22, S4, P4);
	mul(S5, S6, P5);
	mul(S7, S8, P6);
	mul(S9, S10, P7);

	C11(P6, P5, P4, P2);
	add(P2, P1, P2);
	add(P4, P3, P4);
	C22(P5, P1, P3, P7);

	for (i = 0; i < N / 2; i++) {
		for (j = 0; j < N / 2; j++) {
			value[i*N + j] = P6[i*N / 2 + j];
			value[N / 2 + i * N + j] = P2[i*N / 2 + j];
			value[N*N / 2 + i * N + j] = P4[i*N / 2 + j];
			value[N*N / 2 + N / 2 + i * N + j] = P5[i*N / 2 + j];
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

	delete[] A11;
	delete[] A12;
	delete[] A21;
	delete[] A22;
	delete[] B11;
	delete[] B12;
	delete[] B21;
	delete[] B22;
	delete[] S1;
	delete[] S2;
	delete[] S3;
	delete[] S4;
	delete[] S5;
	delete[] S6;
	delete[] S7;
	delete[] S8;
	delete[] S9;
	delete[] S10;
	delete[] P1;
	delete[] P2;
	delete[] P3;
	delete[] P4;
	delete[] P5;
	delete[] P6;
	delete[] P7;
	delete[] value;

	return 0;
}

void add(const int a[], const int b[], int c[]) {
	for (int i = 0; i < N / 2; i++) {
		for (int j = 0; j < N / 2; j++) {
			c[N / 2 * i + j] = a[N * i / 2 + j] + b[N * i / 2 + j];
		}
	}
}

void sub(const int a[], const int b[], int c[]) {
	for (int i = 0; i < N / 2; i++) {
		for (int j = 0; j < N / 2; j++) {
			c[N / 2 * i + j] = a[N * i / 2 + j] - b[N* i / 2 + j];
		}
	}
}

void mul(const int a[], const int b[], int c[]) {
	int done;
	for (int i = 0; i < N / 2; i++) {
		for (int j = 0; j < N / 2; j++) {
			done = 0;
			for (int k = 0; k < N / 2; k++) {
				done = done + a[i * N / 2 + k] * b[j + N * k / 2];
			}
			c[N / 2 * i + j] = done;
		}
	}
}

void C11(int a[], int b[], int c[], int d[]) {
	for (int i = 0; i < N / 2; i++) {
		for (int j = 0; j < N / 2; j++) {
			a[N / 2 * i + j] = a[N * i / 2 + j] + b[N * i / 2 + j] + c[N * i / 2 + j] - d[N * i / 2 + j];
		}
	}
}

void C22(int a[], int b[], int c[], int d[]) {
	for (int i = 0; i < N / 2; i++) {
		for (int j = 0; j < N / 2; j++) {
			a[N / 2 * i + j] = a[N * i / 2 + j] + b[N * i / 2 + j] - c[N * i / 2 + j] - d[N * i / 2 + j];
		}
	}
}
