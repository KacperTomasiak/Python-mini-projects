import random

def get_user_input(message):
  while True:
    try:
      value = int(input(message))
      if value < 0:
        print("Error! Please enter a non-negative value.")
      else:
        return value
    except ValueError:
      print("Error! That's not a valid number. Please try again.")

def update_map(map, width, height):
  for i in range(height):
    for j in range(width):
      num = get_user_input('Type 0 or 1: ')
      while num != 0 and num != 1:
        print('Error! Type 0 or 1!')
        num = get_user_input('Type 0 or 1: ')
      map[i][j] = num

def show_map(map, width, height):
  for i in range(height):
    for j in range(width):
      print(map[i][j], end = ' ')
    print()

def find_islands(map, i, j):
  map[i][j] = 0;
  if i < len(map) - 1 and map[i + 1][j] == 1:
    find_islands(map, i + 1, j)
  if j < len(map[i]) - 1 and map[i][j + 1] == 1:
    find_islands(map, i, j + 1)
  if i > 0 and map[i - 1][j] == 1:
    find_islands(map, i - 1, j)
  if j > 0 and map[i][j - 1] == 1:
    find_islands(map, i, j - 1)

def calculate_islands(map, width, height):
  count = 0
  for i in range(height):
    for j in range(width):
      if map[i][j] == 1:
        find_islands(map, i, j)
        count += 1
  return count

def create_map(map, width, height):
  update_map(map, width, height)
  show_map(map, width, height)
  numberOfIslands = calculate_islands(map, width, height)
  print('Number of islands: ' + str(numberOfIslands))

def generate_map(map, width, height):
  for i in range(height):
    for j in range(width):
      num = random.randint(0, 1)
      map[i][j] = num
  show_map(map, width, height)
  numberOfIslands = calculate_islands(map, width, height)
  print('Number of islands: ' + str(numberOfIslands))

while True:
  width = get_user_input('Type width: ')
  height = get_user_input('Type height: ')
  map = [[0 for x in range(width)] for y in range(height)]
  answer = input('Do you want to enter numbers manually or generate them? [M/A]: ')
  while answer != 'M' and answer != 'A':
    answer = input('Do you want to enter numbers manually or generate them? [M/A]: ')
  if answer == 'M':
    create_map(map, width, height)
  elif answer == 'A':
    generate_map(map, width, height)
  exit = input('Do you want to quit? [Y/N]: ')
  while exit != 'Y' and exit != 'N':
    print('Incorrect value entered!')
    exit = input('Do you want to quit? [Y/N]: ')
  if exit == 'Y':
    break
  elif exit == 'N':
    continue