#is_even(n) returns True or False.

def is_even(num):
  if num%2 == 0:
     return True
  else:
    return False
print(is_even(5))

#average(numbers) takes a list and returns the average
def cal_average(list) :
  return sum(list)/len(list)

list =(2, 4, 5, 7)
print(cal_average(list))