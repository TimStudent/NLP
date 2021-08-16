import matplotlib as matplotlib

import nltk
from nltk.corpus import reuters

# problem 1
nltk.download('reuters')
nltk.download('punkt')
# Question 1) It downloaded the corpus to my C:\users\userid\appdata\roaming\nltk_data directory
# Question 2) the reuters corpus which i downloaded contains 10,788 files
# Question 3) It could be about food. However, I also see some things about debt and interest. I also see various
# various metals. I think it's a dataset of various foods and metals and their various monetary worth worldwide.
print(len(reuters.fileids()))
print(reuters.categories())

# problem 2
print(len(reuters.categories()))
print(len(reuters.sents()))

for x in reuters.categories():
    print(f"Category {x} has {len(reuters.sents(categories=x))} sentences.")

# Question 1) There are 90 categories
# Question 2) There are 54,716 sentences in the reuters corpus
# Question 3) The amount of sentences per category can be seen after running the loop above.

# problem 3

from nltk.corpus import inaugural

word1 = "country"
word2 = "city"
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4]) for fileid in inaugural.fileids() for w in inaugural.words(fileid) for target in [word1, word2]
    if w.lower().startswith(target))
cfd.plot()

# I used the word 'fire' for words that are more popular in recent years and the word 'obama' for words that used to be popular but no longer.

word1 = "fire"
word2 = "obama"
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4]) for fileid in inaugural.fileids() for w in inaugural.words(fileid) for target in [word1, word2]
    if w.lower().startswith(target))
cfd.plot()