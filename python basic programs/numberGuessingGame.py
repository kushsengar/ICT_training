import random
secret_num = random.randint(1,10)
for i in range(1,4):
    guess = int(input("Guess your number :"))
    if guess==secret_num:
        print("You guessed it")
    
print("You ran out of Attempts ")