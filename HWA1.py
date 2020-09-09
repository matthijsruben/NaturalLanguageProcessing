from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
# import nltk
# nltk.download('punkt')  # apparently this was needed for word_tokenize library
# nltk.download('wordnet') # apparently this was needed for WordNetLemmatizer library

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
    return " ".join(stemmed_sentence), stemmed_sentence


wordnet_lemmatizer = WordNetLemmatizer()


def lemmatize_sentence(sentence):
    token_words = word_tokenize(sentence)
    lemmatized_sentence = []
    for element in token_words:
        lemmatized_sentence.append(wordnet_lemmatizer.lemmatize(element, pos="v"))
    return " ".join(lemmatized_sentence), lemmatized_sentence


punctuations = "?:!.,;"
stemmed_piece_of_text = ""
list_of_all_lemmas = []
for sentence in words_list:
    stemmed_sentence = lemmatize_sentence(sentence)
    stemmed_piece_of_text += stemmed_sentence[0]
    for token in stemmed_sentence[1]:
        if token not in punctuations:
            list_of_all_lemmas.append(token)

print(stemmed_piece_of_text)
print(list_of_all_lemmas)
print("Amount of tokens: ", len(list_of_all_lemmas))

amount_tokens = len(list_of_all_lemmas)
for i in range(0, len(list_of_all_lemmas)):
    for k in range(0, i):
        if list_of_all_lemmas[i] == list_of_all_lemmas[k]:
            amount_tokens -= 1
            break
print("Amount of types (unique tokens): ", amount_tokens)