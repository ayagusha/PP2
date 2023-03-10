import time
num = int(input())
after = int(input())
res = num**0.5
time.sleep(after/100)
print(f"Square root of {num} after {after} miliseconds is {res}") 