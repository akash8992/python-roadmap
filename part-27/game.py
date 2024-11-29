print("To quit game enter 0 ")
num = 50
guess = 0
attempt = 0

while guess != num:
    guess = int(input("Guess a number: "))
    if guess == 0:
        attempt += 1

print(f"You guessed it right! in {attempt} attempt")
