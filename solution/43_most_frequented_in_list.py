reviews = ["great", "excellent", "great", "good", "excellent", "excellent"]
word_count = {}

for word in reviews:
    word_count[word] = word_count.get(word, 0) + 1

most_frequent = max(word_count, key=word_count.get)
print(most_frequent)