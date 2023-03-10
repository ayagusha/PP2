mylist = list(input().split())
with open('file.txt', 'w') as f:
    for word in mylist:
    	f.write(word + '\n')
cntnt = open('file.txt')
f.close()
print(cntnt.read())