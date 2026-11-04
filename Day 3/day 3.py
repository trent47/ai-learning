#List = [] ordered and changeable. Duplicates Ok
fruits = ["apple", "banana", "orange", "coconut"]
print(fruits)
print(fruits[1])

for fruit in fruits:
  print(fruit)
print(len(fruits))
print("apple" in fruits)
fruits.append("pineapple")
print(fruits)
fruits.remove("pineapple")
print(fruits)
fruits.insert(0, "pineapple")
fruits.sort()
print(fruits.count("grapes"))

#Set = {} unordered and mutable, but Add/Remove OK. No duplicates

fruits1 = {"apple", "banana", "orange", "coconut"}
fruits1.remove("orange")
print(fruits1)
fruits1.pop()
print(fruits1)

# Tuple = () ordered and unchangeable. Duplicates OK. FASTER
fruits2 = ("apple", "banana", "orange", "coconut")
print(fruits2.index("apple"))


