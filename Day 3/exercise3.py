#Remove duplicates: given [1, 2, 2, 3, 3, 3], make a new list with each number once. Hint: loop and check if item not in new_list.
list = [1, 2, 2, 3, 3, 3]
new_list=[]
for items in list:
  if items not in new_list:
    new_list.append(items)
print(new_list)