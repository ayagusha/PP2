def func(*arr):
    result = 1
    for i in arr:
        result *= i
    return result
    
arr = list(map(int, input().split()))
print(func(*arr))