def palindrome(str1):
    listt = list(str1)
    listt.reverse()
    str2 = ""
    for x in listt:
        str2 += x
    if str2 == str1:
        return True
    else:
        return False
str1 = str(input())
if(palindrome(str1)==True):
    print("A word is palindrome")
else:
    print("A word is not palindrome")