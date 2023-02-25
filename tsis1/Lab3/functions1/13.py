import random
number = 7
cnt = 0
x = 1
y = 21

def func(x,y):
    global r
    r = random.randrange(x,y)
    return r

print("Hello! What is your name?")
name = str(input())
print('Well, ',name,',', ' I am thinking of a number between 1 and 20.', sep = "")
print('Take a guess.')

while(True):
    cnt += 1
    func(x,y)
    print(r)
    if r < number:
        print("Your guess is too low.")
        print("Take a guess.")
        x = r + 1
        y = 21
    elif r > number:
        print("Your guess is too high.")
        print("Take a guess.")
        
        x = 1
        y = r - 1
    else:
        print("Good job, ",name,'!', ' You guessed my number in ',cnt,' guesses!',sep = "")
        break