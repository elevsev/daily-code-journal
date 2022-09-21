from itertools import tee
from FUNCTIONS.data_functions import lemmatisation

text = 'This is a piece of text. My name is Kerryn, and I speak English. Yesterday was my birthday - happy birthday to me!'
print(text)

lemm_text = lemmatisation(texts=text)
print(lemm_text)