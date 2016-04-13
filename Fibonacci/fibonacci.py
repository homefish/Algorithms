'''
Problem:
Print the the first n Fibonacci number,
e.g. for n = 10 the output should be
0 1 1 2 3 5 8 13 21 34

Solution:
Below is a Python 3 program that solves
the problem using a generator.
'''


def fib_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b


def print_first_n_fib_numbers(n):
    for num in fib_generator(n):
        print(num, end = ' ')


def task():
    print_first_n_fib_numbers(10)


if __name__ == '__main__':
    task()
