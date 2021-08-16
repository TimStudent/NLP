# problem 1

import nltk
from nltk.corpus import reuters
nltk.download('reuters')

sentences = (nltk.sent_tokenize(reuters.raw()))
print(len(sentences))
tokens = (nltk.word_tokenize(reuters.raw()))
print(len(tokens))
tps = (len(tokens) / len(sentences))
print("The amount of tokens per sentences is {:.2f}".format(tps))
# a) the amount of tokens per sentences is 30.37.
# b) the category with the largest sentence on average is rye. the category with the smallest sentence on average is acq

list_1 = []
list_2 = []
for x in reuters.categories():
    len_sent = nltk.sent_tokenize(reuters.raw(categories=x))
    list_2.append(x)
    for y in len_sent:
        token_words = nltk.word_tokenize(y)
        tps2 = len(token_words)/len(len_sent)
    list_1.append(tps2)

print(f"The largest tps on average is in category {list_2[(list_1.index(max(list_1)))]} and it is {max(list_1)}")
print(f"The smallest tps on average is in category {list_2[(list_1.index(min(list_1)))]} and it is {min(list_1)}")

# problem 2
book = "1342-0.txt"
f = open(book, 'r', encoding="utf8").read()
book_token_sent = nltk.sent_tokenize(f)
print(len(book_token_sent))

x = open("1342-0.txt", "r", encoding="utf8")
content = x.readlines()
print(f"{len(content)}")

# a) The amount of sentences in the text is 4701. This differs from the readlines by about approximately 10k.
# b) There are three errors. These errors result from 1) human error. 2) it's impossible to write a perfect tokenizer.
# and 3) the contractions words like "it's" and "didn't" make it harder.
