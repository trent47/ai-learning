#Cleaned counter (NLP step): repeat exercise 1, but first make the text lowercase and strip punctuation with .replace(",", "") and .replace(".", ""), so "Hello," and "hello" count as the same word.

sentence = input("Enter your sentence")
sentence = sentence.lower()
sentence = sentence.replace(",","").replace(".","")
words = sentence.split()
counts={}
for word in words:
  counts[word] = counts.get(word, 0) +1
for key,value in counts.items():
  print(key, value)