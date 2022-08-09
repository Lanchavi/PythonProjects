#Password Generator Project
import random
c_letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
s_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_capital_letters= int(input("How many upper case letters would you like in your password?\n"))
nr_small_letters= int(input("How many lower case letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level
password = ""
for letter in range(1, nr_capital_letters + 1):
  clet = random.choice(c_letters)
  password += clet
for letter in range(1, nr_small_letters + 1):
  slet = random.choice(s_letters)
  password += slet
for letter in range(1, nr_symbols + 1):
  sym = random.choice(symbols)
  password += sym
for letter in range(1, nr_numbers + 1):
  num = random.choice(numbers)
  password += num
print(f"Your password is {password}")

#Hard level
passwordl = []
for letter in range(1, nr_small_letters + 1):
  slet = random.choice(s_letters)
  passwordl.append(slet)
for letter in range(1, nr_capital_letters + 1):
  clet = random.choice(c_letters)
  passwordl += clet
for letter in range(1, nr_symbols + 1):
  sym = random.choice(symbols)
  passwordl += sym
for letter in range(1, nr_numbers + 1):
  num = random.choice(numbers)
  passwordl += num  
random.shuffle(passwordl)

password = ""
for letter in passwordl:
  password += letter
print(f"Your password is {password}")

