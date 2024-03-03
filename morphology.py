import spacy
from spacy.lang.en import English
from nltk.stem import PorterStemmer
nlp = spacy.load('en_core_web_sm')
text = "She laughed at the very funny joke."
doc = nlp(text)
print("Morphological Analysis:")
for token in doc:
  print(token.text, "-", token.pos_, "-", token.morph)
stemmer = PorterStemmer()
print("\nStemming:")
for token in doc:
  print(token.text, "-", stemmer.stem(token.text))
