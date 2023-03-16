from sys import stderr

import spacy


def find_best_score_similarity(text, list_of_text):
    if not text or not list_of_text or len(list_of_text) == 0:
        return None
    try:
        nlp = spacy.load('en_core_web_sm')
    except OSError:
        print('Downloading language model for the spaCy POS tagger\n'
            "(don't worry, this will only happen once)", file=stderr)
        from spacy.cli import download
        download('en_core_web_sm')
        nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)
    str_of_text = ' '.join(list_of_text)
    nlp = nlp(str_of_text)
    max_score = 0
    best_match = None
    for token in nlp:
        if doc.similarity(token) > max_score:
            max_score = doc.similarity(token)
            best_match = token.text

    return best_match

find_best_score_similarity("SourceWorkPhone", ["SourceWorkPhone","SourceWorkPhone1","SourceWorkP","SourceWorkPhone123412"])
