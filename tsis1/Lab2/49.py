thislist=["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x if x!="banana" else "orange" for x in thislist]
print(newlist)