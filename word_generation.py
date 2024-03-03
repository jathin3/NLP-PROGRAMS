import random
text = "the quick brown fox jumps over the lazy dog"
order = 2
words = text.split()
freq = {}
for i in range(len(words)-order):
    pair=tuple(words[i:i+order])
    next_word=words[i+order]
    if pair in freq:
        freq[pair][next_word]=freq[pair].get(next_word,0)+1
    else:
        freq[pair]={next_word:1}
start=random.choice(list(freq))
word=list(start)
for i in range(10):
    freq_dist=freq.get(tuple(word[-order:]),{})
    if freq_dist:
        next_word=max(freq_dist,key=freq_dist.get)
        word.append(next_word)
    else:
        break
print(" ".join(words))