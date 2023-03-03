def num(n):
    i=n
    while(i>=0):
        yield i
        i=i-1
    
n=int(input())
for i in num(n):
    print(i)