sentence = input("Enter a text to see word frequency: ").strip()

words = sentence.split(" ")
frequency = {}

for word in words:
    if word not in frequency.keys():
        frequency[word] = 1
    else:
        frequency[word] += 1

print(f"{frequency}")


# alternate solution
# words = sentence.split()
# word_count = {}

# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# print(word_count)