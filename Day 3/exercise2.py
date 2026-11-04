#Reverse a list: build it with a loop or [::-1], and print it
lis = [1,2,3,4,5,6,7]
reverse=[]
for items in lis:
  reverse.insert(0, items)
print(reverse)

reverse1= lis[::-1]
print(reverse1)