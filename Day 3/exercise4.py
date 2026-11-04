#Words in a sentence: ask for a sentence and use .split() to turn it into a list of words. Print the number of words and the longest word. 
#NB :This is your first real NLP step.
sentence= input("Enter your words : " )
words = sentence.split()
print("Words: " ,words)
print("Number of words " ,len(words))

longest =words[0]
for word in words:
  if len(word)>len(longest):
    longest = word
print("Longest word: ",longest)