from itertools import permutations 

def permutation(sttring):

    listt = sttring.split(" ")
    perms = permutations(listt)

    for i in list(perms):
        print(i)
        
sttring = str(input())
permutation(sttring)