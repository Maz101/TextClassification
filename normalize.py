import regex as re 
import spacy

nlp = spacy.load("en_core_web_sm")

def normalizesentence(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'http\S+','',sentence)
    sentence = sentence.replace('-',' ')
    sentence = sentence.replace('|',' ')
    sentence = re.sub(r'[^A-Za-z\s]','',sentence)
    sentence = re.sub(r'\s+', ' ',sentence)
    nlp_output = nlp(sentence)
    nopunct_sentence = []

    for token in nlp_output:
        if token.is_punct or token.lemma_ =="'s":
            continue
        nopunct_sentence.append(token.text)
    

    return ' '.join(nopunct_sentence)
