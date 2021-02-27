import csv
import os
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from words import Words

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
        self.doc = self.nlp(self.data)
        return self.data

    def sentencer(self):
        print("Use self.data and some function ins SpaCy to segment sentence")
        self.sents = []
        for sent in self.doc.sents:
            self.sents.append(sent)
            print(sent)
        return self.sents

    def word(self, stop_word = False):
        self.words = []
        if (stop_word == False):
            for word in self.doc:
                temp = Words()
                temp.text = word.text
                temp.tagging = word.pos_
                self.words.append(temp)
            return self.words
        else:
            for word in self.doc:
                if word.is_stop == False:
                    temp = Words()
                    temp.text = word.text
                    temp.tagging = word.pos_
                    self.words.append(temp)
            return self.words

      #  self.remove_trash_word()
      #  self.determined_word()
      #  self.main_nouns()
       # return self.word

    def determined_word(self):
        self.determined_words = []

    def main_nouns(self):
        self.list_main_noun = []


if __name__ == "__main__":
    test = SimpleNLP(u"/home/nguyen/Documents/muc-tieu-ngan-han/neo4j/test.txt")
    data = test.read_txt()
    words = test.word()
    print(len(words))
    for word in words:
        print(word.text + " " + word.tagging)

    print("Something chnaged")
    remove_words = test.word(True)
    print(len(remove_words))
    for word in remove_words:
        print(word.text + " " + word.tagging)

