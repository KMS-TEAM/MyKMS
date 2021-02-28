from simpleNLP import SimpleNLP

if __name__ == "__main__":
    test = SimpleNLP(u"data/input/wiki_sentences_v2.csv")
    data = test.read_csv()
    test.get_KG()



