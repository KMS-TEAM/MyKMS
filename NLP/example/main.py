from spacy.lang.en import English
import spacy

text = """When learning data science, you shouldn't get discouraged!
Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""

def spacy_tokenizing(text):
    nlp = English()
    my_doc = nlp(text)
    token_list = []
    for token in my_doc:
        token_list.append(token.text)
    print(token_list)

def spacy_sentencizer(text):
    nlp = English()
#    sbd = nlp.create_pipe('sentencizer')
    nlp.add_pipe('sentencizer')
    doc = nlp(text)
    sents_list = []
    for sent in doc.sents:
        sents_list.append(sent.text)
    print(sents_list)

def eng_stop_words(num):
    spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
    print('Number of stop words: %d' % len(spacy_stopwords))
    print('Some stop words example: %s' % list(spacy_stopwords)[:num])


if __name__ == "__main__":
    spacy_tokenizing(text)
    spacy_sentencizer(text)
    eng_stop_words(20)