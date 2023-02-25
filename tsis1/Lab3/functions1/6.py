def reverseFunc(sttring):
    listt = sttring.split(" ")
    listt.reverse()
    for x in listt:
        print(x, end = " ")

sttring = str(input())
reverseFunc(sttring)