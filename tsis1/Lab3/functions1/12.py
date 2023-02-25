def histogram(listt):
    for x in listt:
        for i in range(int(x)):
            print('*', end = "")
        print()
listt = list(input().split())
histogram(listt)