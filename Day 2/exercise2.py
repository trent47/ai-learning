#Number-guessing game: pick a secret number (say 7) and keep asking the user to guess with a while loop. Print "too high" or "too low" until they get it right


actualnum = 7
num =0
while num!=actualnum:
  num = int(input("Enter A Number to guess"))
  if num >actualnum:
    print("Too high")
  else:
    print("Too low")
print("You are Correct! The Secret number is: ", actualnum)