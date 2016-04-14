/*

Problem:
Print the N-th row of Pascal's triangle, e.g.

row 0: 1
row 1: 1 1
row 2: 1 2 1
row 3: 1 3 3 1
row 4: 1 4 6 4 1
row 5: 1 5 10 10 5 1

Solution:
Below is a program in C++11 that solves the problem.

Usage:
Compile with 
g++ -std=c++11 pascal_triangle.cpp -o pascal_triangle.out

and run the executable with
./pascal_triangle.out

*/


#include <bits/stdc++.h>
using namespace std;


string get_Nth_row_Pascal_triangle(int N) {
    vector<int> res;
    if (N == 0) {
        res.push_back(0);
    }
    else {
        vector<int> L;
        L.push_back(1);
        L.push_back(1);
        for (int i = 0; i < N-1; i++) {
            vector<int> L_new;
            L_new.push_back(1);
            for (int k = 0; k < L.size()-1; k++) {
                L_new.push_back(L[k] + L[k+1]);
            }
            L_new.push_back(1);
            L = move(L_new);
        }
        res = L;
    }
    string answer;
    for (auto &num : res) {
        answer.append(to_string(num));
        answer.append(" ");
    }
    return answer;
    
}

int main() {
    for (int i = 0; i < 10; i++) {
        cout << "row " << i << ": " << get_Nth_row_Pascal_triangle(i) << "\n";
    }          
    return 0;
}
