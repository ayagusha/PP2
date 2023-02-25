import math
print('Input number of sides:')
n=int(input())
print('Input the length of a side:')
l=int(input())
p=n*l
x=math.pi/n
s=(n*l**2)/(4*math.tan(x))
print('The area of the polygon is:', int(s))