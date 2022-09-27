import nltk
from nltk.corpus import gutenberg

gutenberg.fileids()

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid)) 
    num_words = len(gutenberg.words(fileid)) 
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(
        "Char/Words:", int(num_chars/num_words), ";", 
        "Words/Sentences:", int(num_words/num_sents), ";", 
        "Words/Vocabulary:", int(num_words/num_vocab), ";",
        "File ID: ", fileid
        )