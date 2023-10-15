import art
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def converttofloat(n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    return n1, n2
def add(n1, n2):
    n1, n2 = converttofloat(n1, n2)
    return float(n1 + n2)
def subtract(n1, n2):
    n1, n2 = converttofloat(n1, n2)
    return float(n1 - n2)
def multiply(n1, n2):
    n1, n2 = converttofloat(n1, n2)
    return float(n1 * n2)
def divide(n1, n2):
    n1, n2 = converttofloat(n1, n2)
    return float(n1 / n2)
def calculate(n1, n2, sign):
    if sign == "+":
        result = add(n1, n2)
        return result
    elif sign == "-":
        result = subtract(n1, n2)
        return result
    elif sign == "*":
        result = multiply(n1, n2)
        return result
    else:
        result = divide(n1, n2)
        return result
# now, to clear the screen
def take_input():
  first_num = input("What's the first number?: ")
  print("+\n-\n*\n/")
  operation = input("Pick an operation?: ")
  next_num = input("What's the next number?: ")
  sum = calculate(first_num, next_num, sign=operation)
  print(f"{first_num} {operation} {next_num} = {sum}")
  decision = input(f"Type 'y' to continue calculating with {sum}, or type 'n' to start a new calculation: ")
  main(decision, sum)
  
def main(decision, sum):
  while decision == 'y':
    first_num = sum
    operation = input("Pick an operation?: ")
    next_num = input("What's the next number?: ")
    sum = calculate(first_num, next_num, sign=operation)
    print(f"{first_num} {operation} {next_num} = {sum}")
    decision = input(f"Type 'y' to continue calculating with {sum}, or type 'n' to start a new calculation: ")
  clear()
  take_input()
  
  
print(art.logo)
take_input()
