'''
Problem:
Compute the greatest common divisor of two integers.

Solution:
Below is a Python 3 program that solves the problem
using the Euclidian algorithm, see
https://en.wikipedia.org/wiki/Euclidean_algorithm#Euclidean_division
'''


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def task():
    # Example
    a, b = 1071, 462
    print("The greatest common divisor of " + str(a) + " and " + str(b) + " is:")
    print(gcd(a,b))


if __name__ == '__main__':
    task()
