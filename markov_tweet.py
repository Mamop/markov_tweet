# -*- coding: utf-8 -*-

import random
from janome.tokenizer import Tokenizer
import tweepy

def wakati(text):
    text = text.replace('\n','')
    text = text.replace('\r','')
    t = Tokenizer()
    result = t.tokenize(text, wakati=True)
    return result

def generate_text(num_sentence=1):
    filename = "markov_text.txt"
    src = open(filename,"r").read()
    wordlist = wakati(src)

    markov = {}
    w1 = ""
    w2 = ""
    for word in wordlist:
        if w1 and w2:
            if (w1,w2) not in markov:
                markov[(w1,w2)] = []
            markov[(w1,w2)].append(word)
        w1, w2 = w2,word

    count_kuten = 0
    num_sentence = num_sentence
    sentence = ""
    w1,w2 = random.choice(list(markov.keys()))
    while count_kuten < num_sentence:
        tmp = random.choice(markov[(w1,w2)])
        sentence += tmp
        if(tmp=='。' or tmp=='！' or tmp=='？'):
            count_kuten += 1
            sentence += '\n'
        w1,w2 = w2,tmp

    CONSUMER_KEY="xxx"
    CONSUMER_SECRET="xxx"
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    ACCESS_TOKEN='xxx'
    ACCESS_SECRET='xxx'
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

    api=tweepy.API(auth)
    api.update_status(sentence[:random.randint(60,90)])


if __name__ == "__main__":
    generate_text()
