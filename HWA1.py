from nltk.stem import PorterStemmer

# create an object of class PorterStemmer
porter = PorterStemmer()

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


