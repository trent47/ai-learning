#Word counter: ask for a sentence, then count how often each word appears and print the result. Hint: loop through the words, then counts[word] = counts.get(word, 0) + 1.

sentence = input("Enter your sentence")
words = sentence.split()

counts = {}
for word in words:
  counts[word] = counts.get(word, 0) +1
for key, value in counts.items():
  print(key, value)
# Top word: from your counts, find and print the most frequent word.
max_word = None
max_count = -1
for key,value in counts.items():
  if value>max_count:
    max_word = key
    max_count = value
print("The most frequent  word is :", max_word , max_count)

