#Ask for a price and a discount percentage, then print the final price.
intial_price = float(input("What is the price of the bike: "))
disc = int(input("Enter the discount percentage :"))
final_price= intial_price-(intial_price*(disc/100))
print("You are going to pay $",final_price)