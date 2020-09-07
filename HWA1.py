from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
# import nltk
# nltk.download('punkt')  # apparently this was needed for word_tokenize library

# create an object of class PorterStemmer
porter = PorterStemmer()

# SORTED_TYPES.txt ----------------------------------------------
print("SORTED_TYPES.txt")
file = open("sorted_types.txt")
words_list = file.readlines()

stemmed_list = []
for word in words_list:
    stemmed_list.append(porter.stem(word[:-1]))

number_types = 0
previous = ""
for stem in stemmed_list:
    if stem != previous:
        number_types += 1
        previous = stem

print("Amount of types (unique words): " + str(number_types))
print("Original word list length: " + str(len(words_list)))

print(words_list)
print(stemmed_list)

# Exercise1_words.txt ----------------------------------------------

print("\n")
print("Words from Exercise 1")
file = open("Exercise1_words.txt")
words_list = file.readlines()

stemmed_list = []
for word in words_list:
    stemmed_list.append(porter.stem(word[:-1]))

number_types = 0
previous = ""
for stem in stemmed_list:
    if stem != previous:
        number_types += 1
        previous = stem

print("Amount of types (unique words): " + str(number_types))
print("Original word list length: " + str(len(words_list)))

print(words_list)
print(stemmed_list)

# Chapter2FirstPage.txt ----------------------------------------------

print("\n")
print("Words of Chapter2FirstPage.txt")

# I removed the " character that was copied from the pdf from the text and replaced it with " in the text file
# I removed the ' character that was copied from the pdf from the text and replaced it with ' in the text file
# It otherwise gave an error
# The contents of the first page of CH2 were copied to a txt.file
file = open("Chapter2FirstPage.txt")
words_list = file.readlines()


def stem_sentence(sentence):
    token_words = word_tokenize(sentence)
    stemmed_sentence = []
    for element in token_words:
        stemmed_sentence.append(porter.stem(element))
    return " ".join(stemmed_sentence)


stemmed_piece_of_text = ""
for sentence in words_list:
    stemmed_sentence = stem_sentence(sentence)
    stemmed_piece_of_text += stemmed_sentence

print("FINAL")
print(stemmed_piece_of_text)

