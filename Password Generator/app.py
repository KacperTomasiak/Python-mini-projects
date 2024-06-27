import string
import secrets

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
chars = letters + digits + symbols
password_length = 12
password = ''

for i in range(password_length):
  password += secrets.choice(chars)

print('Your password: ' + password)