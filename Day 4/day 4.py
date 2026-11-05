#Dictionaries, i watched youtube video: Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs by Corey Schafer

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['name'])
print(student.get('course'))
student['phone']='1311255236'
print(student.get('phone'))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
  print(key, value)