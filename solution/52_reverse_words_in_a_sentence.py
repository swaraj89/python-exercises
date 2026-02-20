sentence = input("Enter a sentence to reverse each word : ")

reverse = " ".join(sentence.split()[::-1])

print(reverse)