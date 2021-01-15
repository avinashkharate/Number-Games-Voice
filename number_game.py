import random
n=random.randint(1,100)
guess=0
print('Enter a number from 1 to 100\n')
    
while (guess<10):
    a=int(input())
    if(a==n):
        print(f'you won in {guess} guesses')
        break
    elif (a>n):
        print('you entered bigger number')
    else:
        print("you entered smaller number")
    print(f"number of guesses reamaining {10-(guess+1)}")
    guess = guess+1

if(guess==10):
    print("You ran out of chances")
