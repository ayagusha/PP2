import re 

s=str(input())
x=re.findall("^[a-z]+_[a-z]+$", s)
print(x)