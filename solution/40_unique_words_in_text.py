sentence = input("Enter a text to see word frequency: ").strip()

unique_words = set(sentence.split())

print(f"{unique_words}")