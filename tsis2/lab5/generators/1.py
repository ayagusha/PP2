def squares(n):
    i=1
    while(i**2<=n):
        yield i**2
        i=i+1
    
n=int(input())
for i in squares(n):
    print(i)