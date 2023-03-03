def f(n):
    i=0
    while(i%3==0 and i%4==0 and i<=n):
        yield i
        i=i+12
    
n=int(input())

for i in f(n):
    print(i)