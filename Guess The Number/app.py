import random

print('Guess The Number')
print('----------------')

def choose_number():
    num = random.randint(1, 10)
    return num

num = choose_number()

while True:
    usr_num = input('Type a number: ')
    if usr_num == 'quit':
        quit()
    elif usr_num.isdigit():
        if int(usr_num) == num:
            print('Congratulations! The number was: ' + str(num))
            print('----------------')
            print('The program has chosen a number from 1 to 10. It is time to guess!')
            num = choose_number()
        else:
            print('You didn\'t manage to guess the number. Try again.')
    else:
        print('Error!')