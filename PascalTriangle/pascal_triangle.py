'''
Problem:
Print the N-th row of Pascal's triangle, e.g.

row 0: 1
row 1: 1 1
row 2: 1 2 1
row 3: 1 3 3 1
row 4: 1 4 6 4 1
row 5: 1 5 10 10 5 1

Solution:
Below is a program in Python 3 that solves the problem.
'''


def get_Nth_line_Pascal_triangle(N):
    if N == 0:
        res = [1]
    else:
        L = [1, 1]
        for k in range(N-1):
            L_new = [1]
            for i in range(len(L)-1):
                L_new.append(L[i] + L[i+1])
            L_new.append(1)
            L = L_new
        res = L
    string_list = [str(c) for c in res]
    return " ".join(string_list)


def task():
    # Example: Print rows 0 to 9 of Pascal's triangle
    for i in range(10):
        print("row " + str(i) + ": " + get_Nth_line_Pascal_triangle(i))


if __name__ == '__main__':
    task()
