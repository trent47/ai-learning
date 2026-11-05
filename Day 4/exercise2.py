#Phone book: a loop that lets the user add names and numbers, or look one up, until they type quit.
"""
pho_book = {}
key = input("Enter the name")
value = input("Enter the phone number")
while key != "quit":
  pho_book.update({key:value})
  key = input("Enter the name")
  value = input("Enter the phone number")
for key, value in pho_book.items():
  print(key, value)
"""
#revised code for correction

phone_book = {}
while True:
  action = input("add, lookup, or quit")
  if action == "add":
    name = input("Name: ")
    phone_book[name] = input("Phone number: ")
  elif action == "lookup":
    name = input("Enter the name: ")
    print(phone_book.get(name, "Not found"))
  elif action == "quit":
    break
  else:
    print("Please type add, lookup, quit")
for name, number in phone_book.items():
  print(na, value)

