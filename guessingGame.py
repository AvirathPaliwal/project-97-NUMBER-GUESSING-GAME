import random
number = random.randrange(1,9)
chans = 0
while chans < 5: 
    guess = int(input("Enter any number: "))
    if guess < number:
        print("Too low")
       # guess = int(input("Enter number again: "))

    elif guess > number:
        print("Too high!")
    #guess = int(input("Enter number again: "))
    else:
        print("you guessed it right!!")
    chans+=1
if not chans < 5:
    print("you loose this is the number" + str(number))
    