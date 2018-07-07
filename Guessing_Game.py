import random
num=random.randint(1,50)

print('Welcome to the Guessing Game')
print("Your job is to choose a number between 1 and 50")
print("If your first guess is within 10, I'll say WARM!")
print("If your first guess is outside of 10, I'll say COLD")
print("If your guess is closer than your previous guess, I'll say WARMER!")
print("If your guess is farther than your previous guess, I'll say COLDER!")
print("LET'S PLAY!")

guesses=[0]

while True:
    guess = int(input('Guess a number between 1 and 50.\nWhat is your guess? '))
    
    if guess < 1 or guess > 50:
        print("OUT OF BOUNDS! Please try again!")
        continue
    
    if guess == num:
        print("Congratulations! You guessed it in only {} guesses!".format(len(guesses)))
        break
    
    guesses.append(guess)
    
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER')
        else:
            print('COLDER')
    else:
        if abs(num-guess) <= 10:
            print('WARM')
        else:
            print('COLD')
            