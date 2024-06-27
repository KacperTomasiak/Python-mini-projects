import random

print('Rock Paper Scissors')
print('-------------------')

choices = ['R', 'P', 'S']
wins = 0

def result():
  computer_choice = random.choice(choices)
  if user_choice == computer_choice:
    return 2
  elif user_choice == 'P' and computer_choice == 'R':
    return 1
  elif user_choice == 'S' and computer_choice == 'P':
    return 1
  elif user_choice == 'R' and computer_choice == 'S':
    return 1
  else:
    return 0

def continue_playing():
  answer = input('Do you want to play again? (Y/N) ').upper()
  if answer == 'N':
    quit()
  elif answer != 'Y':
    while answer != 'Y' or answer != 'N':
      print('Incorrect value entered!')
      answer = input('Do you want to play again? (Y/N) ').upper()
      if answer == 'N':
        quit()
      elif answer == 'Y':
        break

while True:
  user_choice = input('Choose rock (R), paper (P) or scissors (S): ').upper()
  if user_choice == 'R' or user_choice == 'P' or user_choice == 'S':
    if result() == 2:
      print('Draw!')
    elif result() == 1:
      print('You win!')
      wins += 1
    else:
      print('You lose!')
      if wins == 1:
        print('You won ' + str(wins) + ' time.')
      else:    
        print('You won ' + str(wins) + ' times.')
        wins = 0
        continue_playing()
  elif user_choice == 'Q':
    quit()
  else:
    print('Incorrect value entered!')