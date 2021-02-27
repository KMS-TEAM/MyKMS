import csv
import os
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from words import Words
from words import Chunk
class SimpleNLP():

    # Init Simple NLP Object
    def __init__(self, url):
        self.file_url = url
        self.data = ''
        self.graph = []
        self.nlp = spacy.load("en_core_web_sm")

    def read_txt(self):

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

      #  self.determined_word()
      #  self.main_nouns()
       # return self.word
    def noun_chunk(self):
        self.noun_chunk = []
        for chunk in self.doc.noun_chunks:
            temp = Chunk()
            temp.text=chunk.text
            temp.root_text=chunk.root.text
            temp.root_dep=chunk.root.dep_
            temp.root_head_text=chunk.root.head.text
            self.noun_chunk.append(temp)
        return self.noun_chunk

  #  def determined_word(self):
      #  self.determined_words = []

  #  def main_nouns(self):
       # self.list_main_noun = []


if __name__ == "__main__":
    test = SimpleNLP(u"/home/nguyen/Github/MyKMS/NLP/test-chunk.txt")
    data = test.read_txt()
    words = test.word()
    noun_chunks= test.noun_chunk()
    for chunk in noun_chunks:
        print(chunk.text+" "+chunk.root_text+" "+chunk.root_dep)
