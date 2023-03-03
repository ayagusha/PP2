import re 

s=str(input())
x = re.findall("a.*b$", s)
print(x)