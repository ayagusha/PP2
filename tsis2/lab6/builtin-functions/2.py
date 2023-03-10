def lowercnt(st):
    cnt = 0
    for i in st:
        if i.islower():
            cnt += 1
    return cnt

def uppcnt(st):
    cnt = 0
    for i in st:
        if i.isupper():
            cnt += 1
    return cnt

sttr = input()
print(f'num of uppercase: {uppcnt(sttr)}')
print(f'num of lowercase: {lowercnt(sttr)}')