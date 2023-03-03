import re 

s=str(input())
x = re.findall("[A-Z][a-z]+", s)
print(x)