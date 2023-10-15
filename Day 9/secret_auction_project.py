import os
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
flow = ""
flag = False
bid_dictionary = []


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def add_to_list(name, bid):
  bid_dictionary.append({
      "name": name,
      "bid": bid
    })
  
def calculate_maximum_bid(bid_dictionary):
  max = 0
  name_with_max_bid = ""
  for item in bid_dictionary:
    current_item_bid = int(item["bid"])
    if current_item_bid > max:
      max = current_item_bid
      name_with_max_bid = item["name"]
  print(f"The winner is {name_with_max_bid} with a bid of ${max}. ")

def take_input():
  
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  flow = input("Do you want to continue? Type 'Yes' or 'No'\n")
  if(flow.lower() == 'yes'):
    flag = True
    add_to_list(name, bid)
    return flag
  else:
    flag = False
    add_to_list(name, bid)
    calculate_maximum_bid(bid_dictionary)
    return flag

print("Welcome to the secret auction program.")
decision = take_input()
while(decision == True):
  clear()
  decision = take_input()




