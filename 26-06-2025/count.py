def count_word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    print("\nWord Frequencies:")
    for word, count in frequency.items():
        print(f"{word}: {count}")

user_input = input("Enter a sentence: ")
count_word_frequency(user_input)
