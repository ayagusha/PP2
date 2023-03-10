import os

pth = input()
def func1(pth):
	lst = []
	for i in os.listdir(pth):
		if os.path.isdir(os.path.join(pth, i)):
			lst.append(i)
	return lst

def func2(pth):
	lst = []
	for i in os.listdir(pth):
		if os.path.isfile(os.path.join(pth, i)):
			lst.append(i)
	return lst

def func3(pth):
	return os.listdir(pth)

print(*func1(pth))
print(*func2(pth))
print(*func3(pth))