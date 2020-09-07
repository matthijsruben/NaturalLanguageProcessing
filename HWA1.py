from nltk.stem import PorterStemmer

# create an object of class PorterStemmer
porter = PorterStemmer()

print(porter.stem("cats"))
print(porter.stem("trouble"))
print(porter.stem("troubling"))
print(porter.stem("troubled"))

print(porter.stem("called"))
print(porter.stem("call"))
