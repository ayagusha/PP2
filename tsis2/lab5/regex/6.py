import re 

s=str(input())
x = re.sub("\s",",", s) 
y = re.sub("\.",":", x)
print(y)