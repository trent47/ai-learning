#Largest, smallest, average: ask the user for 5 numbers, store them in a list, then print the largest, smallest, and average.

lis = []
count = 0
while count < 5:
  num1 = int(input("Enter your number"))
  lis.append(num1)
  count +=1

print("The largest number is : ", max(lis))
print("The smallest number is : ", min(lis))
print("The average is : ", sum(lis)/len(lis))