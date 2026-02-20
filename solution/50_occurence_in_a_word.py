def look_up(word, sentence):
    return sentence.lower().split(" ").count(word)


sentence = input("Enter a sentence : ")
word = input("Which word are you looking for? ")
count = look_up(word.lower(), sentence)

print(f"The \"{word}\" appears {count} times.")