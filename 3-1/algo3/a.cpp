#include <iostream>
#include <fstream>
#include<string>
#include<vector>
#include <cmath>
#include <cstdlib>
#include<stdio.h>
using namespace std;

void swap(int*, int*);
void quicksort(int, int, int*);
int partitioning(int, int, int*);
void getbinary(int*, int, int, bool, int, int);
void printbinary(int, int);

struct rootnode {
	int left;
	int right;
};

struct word {
	char givenword;
	int value;
	int length;
};

int dictionary[130] = { 0, };
vector <rootnode> tree;
vector <word> result;
int length;

int main() {
	int i, j, k, x, y, count = 0;
	char word;
	int heap[260] = { 0 , };

	ifstream read("input.txt");
	if (read.is_open()) {
		while (!read.eof() && read.get(word)) {
			cout << word;
			dictionary[word]++;
		}
		read.close();
	}

	for (i = 1; i < 129; i++) { if (dictionary[i] != 0) heap[++count] = i; }

	quicksort(1, count, heap);

	for (i = 1; i < 2 * count - 1; i += 2) {
		if (heap[i] > 0) x = dictionary[heap[i]];
		else x = heap[i] * (-1);

		if (heap[i + 1] > 0) y = dictionary[heap[i + 1]];
		else y = heap[i + 1] * (-1);

		for (j = i + 2; j < count + i / 2 + 1; j++) {
			if (heap[j] > 0) {
				if (dictionary[heap[j]] > (x + y)) {
					for (k = count + i / 2 + 1; k > j; k--) { heap[k] = heap[k - 1]; }
					heap[j] = (x + y) * -1;
					break;
				}
			}
			else {
				if (heap[j] * (-1) > (x + y)) {
					for (k = count + i / 2 + 1; k > j; k--) { heap[k] = heap[k - 1]; }
					heap[j] = (x + y) * -1;
					break;
				}
			}
		}
		if (j > count + i / 2) heap[count + i / 2 + 1] = (x + y) * -1;
	}

	y = j;
	k = 1;
	tree.push_back({ 0, 0 });

	while (j > 0) {
		x = 0;
		for (i = 0; i < 2 * k; i++) {
			if (heap[j--] < 0) { tree.push_back({ --y, --y });  x++; }
			else tree.push_back({ 0, 0 });
		}
		k = x;
	}

	length = 2 * count;
	getbinary(heap, 1, 0, false, 0, 0);

	ofstream binfile("compressed.bin", std::ios::out | std::ios::binary | std::ios::app);

	if (binfile) {
		for (i = 1; i < count; i++) {
			cout << result[i].givenword << ":";
			printbinary(result[i].value, result[i].length);
			cout << " ";
			binfile.write((char*)&result[i].givenword, sizeof(char));
			binfile.write((char*)&result[i].value, sizeof(int));
			binfile.write((char*)&result[i].length, sizeof(int));
		}
		cout << endl;

		ifstream read1("input.txt");
		if (read1.is_open()) {
			while (!read1.eof() && read1.get(word)) {
				cout << word;
			}
			read1.close();
		}
		binfile.close();
	}

	ifstream test("compressed.bin");
	if (test.is_open()) {
		while (!test.eof()) {
			for (x = 1; x < count; x++) {
				test.read((char*)&word, sizeof(char));
				test.read((char*)&i, sizeof(int));
				test.read((char*)&j, sizeof(int));
				cout << word << "   " << i << "   " << j << endl;
			}
		}
		test.close();
	}

	return 0;
}

void printbinary(int value, int length) {
	int *binary = new int[length];
	int len = length;

	while (value) {
		if (value == 1) {
			binary[--len] = 1;
			break;
		}

		binary[--len] = value % 2;
		value /= 2;	
	}

	for (int i = 0; i < length; i++) { 
		if (binary[i] != 1) cout << 0;
		else cout << binary[i]; }
	delete[] binary;
}

void getbinary(int* heap, int root, int count, bool preside, int value, int number) {
	if (heap[length - root] < 0) {
		if (tree[root].left != 0) getbinary(heap, length - tree[root].left, count, false, 2 * value + 1, number + 1);
		if (tree[root].right != 0) getbinary(heap, length - tree[root].right, count, true, 2 * value, number + 1);
	}

	else result.push_back({ (char)heap[length - root] , value, number});
}

void  quicksort(int first, int last, int* besort) {
	if (first < last) {
		int i = partitioning(first, last, besort);
		quicksort(i + 1, last, besort);
		quicksort(first, i - 1, besort);
	}
}

int partitioning(int first, int last, int* besort) {
	int i = first;
	int j;
	for (j = first; j < last; j++) {
		if (dictionary[besort[last]] > dictionary[besort[j]]) {
			swap(&besort[i++], &besort[j]);
		}
	}
	swap(&besort[i], &besort[j]);
	return i;
}

void swap(int *a, int *b) {
	int swap;
	swap = *a;
	*a = *b;
	*b = swap;
}

