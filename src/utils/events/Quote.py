# modules for generating random quotes and nlp
from random import randint
from quote import quote
import nltk
from random_word import RandomWords
from src.utils.events.Learn import get_synonyms




def get_quote_from_word(word):
    res = quote(word, limit=1)
    tries = 0
    limit = 5
    def_word = 'joy'
    while type(res) == type(None) or len(res) < 1:
        res = quote(word, limit=1)
        if tries >= limit:
            return quote(def_word, limit=1)
        tries += 1

    return res


def get_quote_from_rand_word():
    r = RandomWords()
    word = r.get_random_word()
    return get_quote_from_word(word)


# properly prints a quote object
def print_quote(quote, speaker='Daemona'):
    quote = quote[0]
    print()
    print(speaker + ": Here's a quote by " + quote['author'] + ".")
    print()
    print(quote['quote'])

def get_synonym(word):
    synonyms = get_synonyms(word)
    length = len(synonyms)
    return synonyms[randint(0, length)] if length > 0 else word


def get_quote_from_synonym(word):
    return get_quote_from_word(get_synonym(word))

# get a quote from adjective using nlp


def get_quote_from_statement(statement):
    # analyze statement
    text = nltk.word_tokenize(text)
    result = nltk.pos_tag(text)
    print(text)
