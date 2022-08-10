#Simple_Calculator

#Addition
def add(n1, n2):
  return n1 + n2
#Subtraction
def sub(n1, n2):
  return n1 - n2
#Division
def div(n1, n2):
  return n1 / n2
#Multiplication
def mul(n1, n2):
  return n1 * n2

calc = {
  "+" : add,
  "-" : sub,
  "/" : div,
  "*" : mul,
}

num1 = float(input("What is the first num: "))
num2 = float(input("What is the second num: "))
for symbol in calc:
  print(symbol)
operation = input("Choose a operation from the above sysmbols: ")
calculation = calc[operation]
ans = calculation(num1 , num2)
print(f"{num1} {operation} {num2} = {ans}")

more_calc = input("Want to procced with calculations, y or n: ")

if more_calc == "y":
  num3 = float(input("What is the third num: "))
  new_operation = input("Pick the operation: ")
  new_calculation = calc[new_operation]
  new_ans = new_calculation(ans , num3)
  print(f"{ans} {new_operation} {num3} = {new_ans}")
else:
  print("exit")
