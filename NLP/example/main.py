from spacy.lang.en import English
import spacy

text = """When learning data science, you shouldn't get discouraged!
Challenges and setbacks aren't failures, they're just part of the journey. You've got this!"""

def spacy_tokenizing(nlp, text):
    my_doc = nlp(text)
    token_list = []
    for token in my_doc:
        token_list.append(token.text)
    print(token_list)

def spacy_sentencizer(nlp, text):
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

def remove_stopwords(nlp, text):
    filtered_sent = []
    doc = nlp(text)

    for word in doc:
        if word.is_stop == False:
            filtered_sent.append(word)
    return filtered_sent

if __name__ == "__main__":
    nlp = English()
    spacy_tokenizing(nlp, text)
    spacy_sentencizer(nlp, text)
    eng_stop_words(20)
    print(remove_stopwords(nlp, text))