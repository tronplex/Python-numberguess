import random

number_pool = range(1,6)
secret_number = random.choice(number_pool)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess the number between 1 and 5: '))
    guess_count += 1
    if guess == secret_number:
        print('You got it!')
        break
else:
    print(f'Sorry, the number was {secret_number}. Try again :(')
