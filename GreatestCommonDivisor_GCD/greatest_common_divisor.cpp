/*
Problem:
Compute the greatest common divisor of two integers.

Solution:
Below is a C++11 program that solves the problem
using the Euclidian algorithm, see
https://en.wikipedia.org/wiki/Euclidean_algorithm#Euclidean_division
*/


#include <bits/stdc++.h>
using namespace std;


int gcd(int a, int b) {
    if (b == 0) return a;
    else return gcd(b, a%b);
}


int main() {
    // Example
    int a = 1071;
    int b = 462;
    cout << "The greatest common divisor of " << a << " and " << b << " is:\n";
    cout << gcd(a,b) << "\n";
    
    return 0;
}
