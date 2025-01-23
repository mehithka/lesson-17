import random
playing = True
number = str(random.randint(10,20)) 

print("I will select a number at random from 10-20 and you have to guess that number each time")
print("the game ends when you get 1 hero!")

while playing:
    guess=str(input("Guess a random number. "))
    if number == guess:
        print("Nice one you win")
        print("the number was: ", number)
        break
    else:
        print("thats not right try again!",'\n')
