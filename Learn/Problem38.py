import random
a=random.uniform(0,100)
a=a // 1
print("MINIGAME: Guess the number between 0 and 100")
while True:
    b=int(input("Enter your guess:"))
    if b>a:
        print("Your guess is too high")
    elif b<a:
        print("Your guess is too low")
    else:
        print("You guessed it right!")
        break   