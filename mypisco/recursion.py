def sum_array(array):
    return sum(array)


def fibonacci(n):

    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):
    result = word[::-1]
    return result