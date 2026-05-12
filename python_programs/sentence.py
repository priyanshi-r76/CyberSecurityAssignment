# Program to analyze a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()

vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

for char in sentence:

    if char.isalpha():

        if char in vowels:
            vowel_count += 1

        else:
            consonant_count += 1

word_frequency = {}

for word in words:

    if word in word_frequency:
        word_frequency[word] += 1

    else:
        word_frequency[word] = 1

print("Total Words:", len(words))
print("Total Vowels:", vowel_count)
print("Total Consonants:", consonant_count)

print("Word Frequency:")

for word, count in word_frequency.items():
    print(word, ":", count)
