import nltk
nltk.download('punkt')
sentense="There's a good chance you've interacted with NLP in the form of voice-operated GPS systems,digital assistants,speech-to-text dictation software,customers service chatbots,and other consumer conveniences"
words=nltk.word_tokenize(sentense)
print(words)
word_freq=nltk.FreqDist(words)
print('most common words:',word_freq.most_common(3))
most_common_words:[('natural',1),('language',1),('processing',1)]
word_freq.plot(30,cumulative=False)
import nltk
from nltk.probability import FreqDist
text1="Natural language processing (NLP) is the ability of a computer program to understand human language as it's spoken and written -- referred to as natural language. It's a component of artificial intelligence ."
print(text1)
word_token=nltk.word_tokenize(text1)
print(word_token)
len(word_token)
word2=FreqDist(word_token)
print(word2)
len(word2)
word2.most_common(10)
word2.most_common(5)
word2.most_common(15)
word2.freq("NLP")
word2.freq("for")
word2.freq(",")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(10,5))
word2.plot(10)
def generate_ngrams(text,n):
    words=text.split()
    ngrams=[tuple(words[i:i+n]) for i in range(len(words)-n+1)]
    return ngrams
def main():
    text=input()
    n=int(input())
    ngrams=generate_ngrams(text,n)
    print(f"{n}-ngrams:")
    for gram in ngrams:
        print(gram)
if __name__=="__main__":
    main()
