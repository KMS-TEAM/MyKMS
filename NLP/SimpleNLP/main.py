import csv
import os
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
class SimpleNLP():

    # Init Simple NLP Object
    def __init__(self, url):
        self.file_url = url
        self.data = ''
        self.graph = []
        self.nlp = spacy.load("en_core_web_sm")

    def read_txt(self):
        self.file_url = '/home/nguyen/Documents/muc-tieu-ngan-han/neo4j/test.txt'
        fd =  open(self.file_url,mode ='r', encoding='utf-8')
        self.data = fd.read().strip()
        return self.data

    def sentencer(self):
        doc = self.nlp(self.data)
        print(type(doc))
        self.sent = []
        for sent in doc.sents:
            self.sent.append(sent)
            print(sent)
        return self.sent
        print("Use self.data and some function ins SpaCy to segment sentence")

    def word(self):
        doc = self.nlp(self.data)
        self.words = []
        for word in doc:
            self.words.append(word.text)
        return self.words

      #  self.remove_trash_word()
      #  self.determined_word()
      #  self.main_nouns()
       # return self.word

    def remove_trash_word(self):
        self.removed_trash_word = []
        doc = self.nlp(self.data)
        for word in doc:
            if word.is_stop == False:
                self.removed_trash_word.append(word)
        return self.removed_trash_word
    def determined_word(self):
        self.determined_words = []

    def main_nouns(self):
        self.list_main_noun = []


if __name__ == "__main__":
    test = SimpleNLP(u"/home/nguyen/Documents/muc-tieu-ngan-han/neo4j/test.txt")
    data = test.read_txt()
    text = test.sentencer()
    words = test.word()
    stop_word = test.remove_trash_word()
    for word in stop_word:
        print(word)

