# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1

    for i in range(1, n+1):
        result = result * (i)
    return result;

def factorial_recursive(n):
    if (n <= 1) : return 1

    return n * factorial_recursive(n-1)

print(factorial_iterative(3))
print(factorial_recursive(3))
