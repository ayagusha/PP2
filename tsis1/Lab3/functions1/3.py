def solve(numheads, numlegs):
    for a in range(1,numheads+1):
        for b in range(1,numlegs+1):
            if a+b==numheads and (2*a)+(4*b)==numlegs:
                print(a,b)
                break
            else: 
                continue
solve(35,94)        