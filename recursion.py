def sum_array(array):
    return sum(array)
print(sum_array([2,14,25]))

def fibonacci(n):

    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(8))

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
print(factorial(5))

def reverse(word):
    result = word[::-1]
    return result
[print(reverse("This is a string you need to reverse"))]