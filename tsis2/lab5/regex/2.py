import re 

s=str(input())
x =re.findall("a.{2,3}b", s)
print(x)