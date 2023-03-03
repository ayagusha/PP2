def squares(a, b):
    i=a
    while(i**2<=b):
        yield i**2
        i=i+1
    
a=int(input())
b=int(input())
for i in squares(a, b):
    print(i)