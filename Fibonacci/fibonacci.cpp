/*
Problem:
Print the the first n Fibonacci number,
e.g. for n = 10 the output should be
0 1 1 2 3 5 8 13 21 34

Solution:
Below is a C++11 program that solves the problem.
*/


#include <bits/stdc++.h>
using namespace std;

void print_first_n_fibonacci_numbers(int n) {
    int a = 0;
    int b = 1;
    int c;
    for (int i = 0; i < n; i++) {
        cout << a << " ";
        c = a + b;
        a = b;
        b = c;
    }
    cout << "\n";
}


int main() {
    // Example
    print_first_n_fibonacci_numbers(10);
    return 0;
}
