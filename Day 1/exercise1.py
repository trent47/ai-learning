#Ask for two numbers and print their sum, difference, and product. .
#Ask for a sentence and print it in uppercase  and its length .
#Ask for a price and a discount percentage, then print the final price. 
#Exercise Code 1
num1 = int(input("Enter your First Number : "))
num2 = int(input("Enter your Second Number : "))
total= num1+num2
if num1 >num2:
  differ = num1-num2
elif num1 >num2:
  differ = num2-num1
else:
  differ = 0
pro = num1*num2
print("The Sum is : ", total)
print("The difference is : ", differ)
print("The product is : ", pro)
