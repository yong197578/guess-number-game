
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

# Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
# Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
# Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

# Let the user guess a number.
    guess = int(input("Make a guess: "))

# Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()


# import random
# from art import logo
# print(logo)
#
#
# print("Welcome to the Number Guess Game!")
# random_number = random.randint(1, 100)
# print(random_number)
# ease_or_hard = input("I am thinking of a number between 1 to 100.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
# if ease_or_hard == "easy":
#     life_remaining = 10
# elif ease_or_hard == 'hard':
#     life_remaining = 5
#
# continue_game = False
# while not continue_game:
#     print(f"You have {life_remaining} attempts remaining to guess the number")
#     user_input = int(input("Make a Guess: "))
#     if user_input == random_number:
#         print(f"You guessed {random_number}. Congradulation!")
#         continue_game = True
#     elif life_remaining == 1:
#         print("You used all attempts. Game Over!")
#         continue_game = True
#     elif user_input > random_number:
#         print("Too High")
#         life_remaining -= 1
#         continue_game = False
#     elif user_input < random_number:
#         print("Too low")
#         life_remaining -= 1
#         continue_game = False
