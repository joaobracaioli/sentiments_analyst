#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Install TextBlob

pip install -U textblob
"""


from textblob import TextBlob
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

blob = TextBlob(text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

media_sentimento = []

for words, tag in blob.tags:
    print (words, tag)

for sentence in blob.sentences:
    print(sentence)
    polariry = sentence.sentiment.polarity
    media_sentimento.append(polariry)
    print(polariry)



print('MÉDIA DE SENTIMENTO: ' + str(np.mean(media_sentimento)))