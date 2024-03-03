import nltk
from nltk.corpus import treebank
# Step 1: Load the Treebank corpus
nltk.download('treebank')
nltk.download('punkt')
# Step 2: Prepare the training data
train_data = treebank.tagged_sents()[:3000]  # Use first 3000 sentences for training
# Step 3: Train the POS tagger on the Treebank corpus
tagger = nltk.HiddenMarkovModelTagger.train(train_data)
# Step 4: Test the POS tagger
test_sentence = "This is a sample sentence"
tokenized_sentence = nltk.word_tokenize(test_sentence)
tagged_sentence = tagger.tag(tokenized_sentence)
# Step 5: Display the tagged sentence
print("Tagged Sentence:", tagged_sentence)
