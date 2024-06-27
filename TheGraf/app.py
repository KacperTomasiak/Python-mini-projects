from random import randint

file = open("quotes.txt", "r")
data = []

already_added = []

for line in file:
  data.append(line.strip())

num = randint(1, 5);

for i in range(num):
  quote_index = randint(0, len(data) - 1)
  while quote_index in already_added:
    quote_index = randint(0, len(data) - 1)
  print(data[quote_index])
  already_added.append(quote_index)
  if i != num - 1:
    print()