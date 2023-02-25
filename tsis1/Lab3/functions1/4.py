def filter_prime(list1): 
    list2 = [] 
    for x in list1: 
        m = l = int(x) 
        cnt = 0 
        for i in range(1,m+1): 
            if l == 1: 
                list2.append(l) 
            if l % i == 0: 
                cnt += 1 
            else: 
                continue 
        if cnt == 2: 
            list2.append(l) 
        else: 
            continue 
    print(list2) 
 
list1 = list(input().split()) 
filter_prime(list1)