import art
import game_data
import random
import os

A = 'A'
B = 'B'


def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


list = list(range(0, 50))


def get_info(follower, indicator):
  number_A = random.choice(list)
  follower = game_data.data[number_A]
  print(
    f"Compare {indicator}: {follower['name']}, {follower['description']}, from {follower['country']}"
  )
  return follower


def check(choice, follower_A, follower_B, current_score):
  if choice == 'A' and follower_A['follower_count'] > follower_B[
      'follower_count']:
    current_score += 1
    clear()
    print(art.logo)
    print(f"You are correct. Current score {current_score}")
    wrong_ans_flag = False
    return wrong_ans_flag, current_score
  elif choice == 'A' and follower_A['follower_count'] < follower_B[
      'follower_count']:
    wrong_ans_flag = True
    clear()
    print(art.logo)
    return wrong_ans_flag, current_score
    # print(f"Sorry that's wrong. Final score {current_score}!")
  elif choice == 'B' and follower_B['follower_count'] > follower_A[
      'follower_count']:
    current_score += 1
    clear()
    print(art.logo)
    print(f"You are correct. Current score {current_score}")
    wrong_ans_flag = False
    return wrong_ans_flag, current_score
  elif choice == 'B' and follower_B['follower_count'] < follower_A[
      'follower_count']:
    wrong_ans_flag = True
    clear()
    print(art.logo)
    return wrong_ans_flag, current_score
  else:
    pass


def start_game():
  print(art.logo)
  current_score = 0
  wrong_ans_count = 0
  wrong_ans_flag = False
  follower_A = {}
  follower_B = {}
  while not wrong_ans_flag:
    follower_A = get_info(follower_A, A)
    print(art.vs)
    follower_B = get_info(follower_B, B)
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == 'A':
      wrong_ans_flag, current_score = check(choice, follower_A, follower_B,
                                            current_score)
    elif choice == 'B':
      wrong_ans_flag, current_score = check(choice, follower_A, follower_B,
                                            current_score)

  print(f"Sorry that's wrong. Final score {current_score}!")
  current_score = 0

  choice = input('Do you want to play again? Type y or n: ')
  while choice == 'y':
    clear()
    start_game()
    choice = input('Do you want to play again? Type y or n: ')


start_game()

# print(f"Against B: {name_A}, {description_A}, from {nationality_A}")
