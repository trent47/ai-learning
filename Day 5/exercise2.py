#clean_text(text) returns the text lowercased with , and . removed (from Day 4)
def clean_text(text):
  text = text.lower()
  text = text.replace(",","").replace(".","")
  return text.split()

#count_words(text) returns a dictionary of word counts. Inside it, call clean_text()
def count_words(text):
  words = clean_text(text)
  counts = {}
  for word in words:
    counts[word] = counts.get(word, 0) + 1
  return counts

#top_word(counts) takes that dictionary and returns the most frequent word.
def top_word(counts):         
  max_count=-1
  max_word = None
  for word, value in counts.items():
    if value > max_count:
      max_word = word
      max_count = value
  return max_word, max_count

text = input("Enter your sentence")
print(top_word(count_words(text)))

