from nltk.corpus import brown 
from nltk.corpus import inaugural
import nltk

cfd = nltk.ConditionalFreqDist(
    (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))

print(cfd)

genre_word = [(genre, word)
                for genre in ['news', 'romance']
                for word in brown.words(categories=genre)]

print(genre_word[:10])
