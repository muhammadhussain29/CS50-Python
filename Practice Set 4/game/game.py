import random 

level = input("Level: ")
while True:
    try:
        level = int(level)
        if level < 0:
            raise ValueError
        break
    except ValueError:
        level = input("Level: ")

ans = random.randint(0,level)
guess = input("Guess: ")
while True:
    try:
        guess = int(guess)
        if guess == ans:
            print("Just right!")
            break
        elif guess > ans:
            print("Too large!")  
            raise ValueError  
        elif guess < ans:
            print("Too small!")
            raise ValueError  
        else:
            raise ValueError
    except ValueError:
        guess = input("Guess: ")

    
