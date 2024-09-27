sen = input("Enter Sentence : ")
words = sen.split()
counts = {}

for words in words:
  words = words.lower()
  if words in counts:
    counts[words] += 1
  else:
    counts[words] = 1

for  words, counts in counts.items():
  print(f"{words} : {counts}")